import { BastionHostLinux, InterfaceVpcEndpointAwsService, Vpc } from '@aws-cdk/aws-ec2';
import { AwsLogDriver, CfnTaskDefinition, Cluster, ContainerImage, Ec2TaskDefinition, ExternalService, ExternalTaskDefinition, PropagatedTagSource } from '@aws-cdk/aws-ecs';
import { ApplicationListener, ApplicationLoadBalancer, ApplicationProtocol, ApplicationTargetGroup, TargetType } from '@aws-cdk/aws-elasticloadbalancingv2';
import { Rule } from '@aws-cdk/aws-events';
import { LambdaFunction } from '@aws-cdk/aws-events-targets';
import { ManagedPolicy, Role, ServicePrincipal } from '@aws-cdk/aws-iam';
import { Code, Function, Runtime } from '@aws-cdk/aws-lambda';
import * as cdk from '@aws-cdk/core';
import { CfnOutput, CfnParameter, Stack, Tags } from '@aws-cdk/core';
import { ApplicationLoadBalancedExternalService } from './alb-external-service';

export class AnywhereStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const clientCertificateArn = new CfnParameter(this, 'clientCertificateArn', { default: 'arn:aws:acm:eu-west-1:693196418513:certificate/6f2a2ccb-27b3-41b5-b43f-e1015345e042' });
    const serverCertificateArn = new CfnParameter(this, 'serverCertificateArn', { default: 'arn:aws:acm:eu-west-1:693196418513:certificate/72f82f5f-a1b2-4609-b769-e4055fc77027' });
    const vpc = new Vpc(this, 'testVpc', {
      cidr: '10.12.14.0/23',
      natGateways: 0
    });

    vpc.addInterfaceEndpoint('ssmEndpoint', { service: InterfaceVpcEndpointAwsService.SSM });
    vpc.addInterfaceEndpoint('ssmMessagesEndpoint', { service: InterfaceVpcEndpointAwsService.SSM_MESSAGES });
    vpc.addInterfaceEndpoint('ec2MessagesEndpoint', { service: InterfaceVpcEndpointAwsService.EC2_MESSAGES });

    const clientVpnEndpoint = vpc.addClientVpnEndpoint('clientVpn', {
      cidr: '10.15.16.0/22',
      serverCertificateArn: serverCertificateArn.valueAsString,
      clientCertificateArn: clientCertificateArn.valueAsString
    });

    clientVpnEndpoint.addAuthorizationRule('onpremAuthRule', { cidr: '10.211.55.0/24' });

    new CfnOutput(this, 'Endpoint', {
      value: `v.${clientVpnEndpoint.endpointId}.prod.clientvpn.${Stack.of(this).region}.amazonaws.com`,
      description: 'Client VPN endpoint DNS name'
    });

    const bastion = new BastionHostLinux(this, 'bastion', { vpc: vpc });

    const cluster = new Cluster(this, 'testCluster', { vpc: vpc, clusterName: 'AnywhereCluster' });

    const service = new ApplicationLoadBalancedExternalService(this, 'albService', {
      cluster: cluster,
      cpu: 100,
      memoryLimitMiB: 100,
      desiredCount: 1,
      openListener: true,
      protocol: ApplicationProtocol.HTTP,
      taskImageOptions: {
        image: ContainerImage.fromRegistry('nginx'),
        containerPort: 80,
        enableLogging: true
      }
    });

    const tgArn = service.targetGroup.targetGroupArn;
    Tags.of(service).add('targetGroup', tgArn, { includeResourceTypes: ['AWS::ECS::Service'] });

    const ecsExternalInstanceRole = new Role(this, 'ecsExternalInstanceRole', {
      roleName: 'ecsExternalInstanceRole',
      assumedBy: new ServicePrincipal('ssm.amazonaws.com'),
      managedPolicies: [
        ManagedPolicy.fromAwsManagedPolicyName('AmazonSSMManagedInstanceCore'),
        ManagedPolicy.fromAwsManagedPolicyName('service-role/AmazonEC2ContainerServiceforEC2Role'),
        ManagedPolicy.fromAwsManagedPolicyName('CloudWatchLogsFullAccess')
      ]
    });

    const taskFunction = new Function(this, 'taskFunction', {
      code: Code.fromAsset('task_function'),
      handler: 'task.statechange.lambda_handler',
      runtime: Runtime.PYTHON_3_8,
      environment: {
        'targetGroup': tgArn
      }
    });
    
    ['AmazonECS_FullAccess', 'AmazonSSMFullAccess', 'ElasticLoadBalancingFullAccess'].forEach(policy =>
      taskFunction.role?.addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policy))
    );

    Object.entries({ 'startTask': 'RUNNING', 'stopTask': 'STOPPED' }).forEach(entry =>
      new Rule(this, entry[0], {
        ruleName: entry[0],
        targets: [new LambdaFunction(taskFunction)],
        eventPattern: {
          detailType: ['ECS Task State Change'],
          source: ['aws.ecs'],
          detail: {
            desiredStatus: [entry[1]],
            lastStatus: [entry[1]],
            clusterArn: [cluster.clusterArn]
          }
        }
      }));
  }
}
