import { BastionHostLinux, InterfaceVpcEndpointAwsService, Vpc } from '@aws-cdk/aws-ec2';
import { CfnTaskDefinition, Cluster, ContainerImage, Ec2TaskDefinition, PropagatedTagSource } from '@aws-cdk/aws-ecs';
import { ApplicationListener, ApplicationLoadBalancer, ApplicationProtocol, ApplicationTargetGroup, TargetType } from '@aws-cdk/aws-elasticloadbalancingv2';
import { Rule } from '@aws-cdk/aws-events';
import { LambdaFunction } from '@aws-cdk/aws-events-targets';
import { ManagedPolicy, Role, ServicePrincipal } from '@aws-cdk/aws-iam';
import { Code, Function, Runtime } from '@aws-cdk/aws-lambda';
import * as cdk from '@aws-cdk/core';
import { CfnOutput, CfnParameter, Stack, Tags } from '@aws-cdk/core';
import { AnywhereService } from './anywhere-service';

export class AnywhereStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const clientCertificateArn = new CfnParameter(this,'clientCertificateArn', { default: 'arn:aws:acm:eu-west-1:693196418513:certificate/6f2a2ccb-27b3-41b5-b43f-e1015345e042'});
    const serverCertificateArn = new CfnParameter(this,'serverCertificateArn', { default: 'arn:aws:acm:eu-west-1:693196418513:certificate/72f82f5f-a1b2-4609-b769-e4055fc77027'});
    const vpc = new Vpc(this,'testVpc',{
      cidr: '10.12.14.0/23',
      natGateways:0
    });

    vpc.addInterfaceEndpoint('ssmEndpoint',{service: InterfaceVpcEndpointAwsService.SSM});
    vpc.addInterfaceEndpoint('ssmMessagesEndpoint',{service: InterfaceVpcEndpointAwsService.SSM_MESSAGES});
    vpc.addInterfaceEndpoint('ec2MessagesEndpoint',{service: InterfaceVpcEndpointAwsService.EC2_MESSAGES});

    const clientVpnEndpoint = vpc.addClientVpnEndpoint('clientVpn',{
      cidr: '10.15.16.0/22',
      serverCertificateArn: serverCertificateArn.valueAsString,
      clientCertificateArn: clientCertificateArn.valueAsString
    });

    clientVpnEndpoint.addAuthorizationRule('onpremAuthRule',{cidr: '10.211.55.0/24'});

    new CfnOutput(this, 'Endpoint', {
      value: `v.${clientVpnEndpoint.endpointId}.prod.clientvpn.${Stack.of(this).region}.amazonaws.com`,
      description: 'Client VPN endpoint DNS name'
    });

    const bastion = new BastionHostLinux(this,'bastion',{vpc: vpc});
    
    const alb = new ApplicationLoadBalancer(this, 'alb', {
      vpc: vpc,
      internetFacing: true
    });
    
    const tg = new ApplicationTargetGroup(this,'tg',{
      protocol: ApplicationProtocol.HTTP,
      vpc: vpc,
      targetType: TargetType.IP
    });
    tg.configureHealthCheck({enabled: true});
    const listener = new ApplicationListener(this,'listener', {
      loadBalancer: alb,
      protocol: ApplicationProtocol.HTTP,
      defaultTargetGroups: [tg]
    });

    const cluster = new Cluster(this,'testCluster',{ vpc: vpc, clusterName: 'AnywhereCluster'});

    const taskExecutionRole = new Role(this,'taskExecutionRole',{
      assumedBy: new ServicePrincipal('ecs-tasks.amazonaws.com')
    });

    [ 'AmazonAPIGatewayInvokeFullAccess', 'service-role/AmazonECSTaskExecutionRolePolicy', 'AmazonEC2ContainerRegistryReadOnly',
      'AmazonSSMReadOnlyAccess', 'AmazonS3ReadOnlyAccess', 'AmazonDynamoDBReadOnlyAccess', 'service-role/AWSLambdaRole',
      'AmazonECS_FullAccess', 'AmazonSSMFullAccess', 'ElasticLoadBalancingFullAccess'
    ].forEach(policy =>
      taskExecutionRole.addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policy))
    );

    const taskDef = new Ec2TaskDefinition(this,'taskDef',{
      executionRole: taskExecutionRole
    });
    taskDef.addContainer('nginx',{
      image: ContainerImage.fromRegistry('nginx'),
      memoryLimitMiB: 1024,
      cpu: 1024,
      portMappings: [ { containerPort: 80}]
    });
    
    (taskDef.node.defaultChild as CfnTaskDefinition).addPropertyOverride('RequiresCompatibilities',['EXTERNAL']);

    [ 'service-role/AmazonECSTaskExecutionRolePolicy', 'AmazonS3ReadOnlyAccess', 
      'AmazonDynamoDBReadOnlyAccess', 'service-role/AWSLambdaRole'
    ].forEach(policy =>
      taskDef.taskRole.addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policy))
    );
    const service = new AnywhereService(this, 'testService', {
      cluster: cluster,
      taskDefinition: taskDef,
      serviceName: 'nginx',
      desiredCount: 0,
      propagateTags: PropagatedTagSource.SERVICE
    });
    Tags.of(service).add('targetGroup',tg.targetGroupArn);

    const ecsExternalInstanceRole = new Role(this,'ecsExternalInstanceRole',{
      roleName: 'ecsExternalInstanceRole',
      assumedBy: new ServicePrincipal('ssm.amazonaws.com'),
      managedPolicies: [ 
        ManagedPolicy.fromAwsManagedPolicyName('AmazonSSMManagedInstanceCore'),
        ManagedPolicy.fromAwsManagedPolicyName('service-role/AmazonEC2ContainerServiceforEC2Role')
      ]
    });

    const taskFunction = new Function(this,'taskFunction',{
      code: Code.fromAsset('task_function'),
      handler: 'task.statechange.lambda_handler',
      runtime: Runtime.PYTHON_3_8,
      environment: {
        'targetGroup': tg.targetGroupArn
      }
    });

    ['AmazonECS_FullAccess', 'AmazonSSMFullAccess', 'ElasticLoadBalancingFullAccess'].forEach(policy =>
      taskFunction.role?.addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policy))
    );

    new Rule(this,'changedTask',{
      ruleName: 'ChangedTask',
      targets: [ new LambdaFunction(taskFunction)],
      eventPattern: {
        detailType: ['ECS Task State Change'],
        source: ['aws.ecs'],
        detail:{
          desiredStatus: ['STOPPED'],
          lastStatus: ['STOPPED'],
          clusterArn: [cluster.clusterArn]
        }
      }
    });

    new Rule(this,'startTask',{
      ruleName: 'StartTask',
      targets: [ new LambdaFunction(taskFunction)],
      eventPattern: {
        detailType: ['ECS Task State Change'],
        source: ['aws.ecs'],
        detail:{
          desiredStatus: ['RUNNING'],
          lastStatus: ['RUNNING'],
          clusterArn: [cluster.clusterArn]
        }
      }
    });
  }
}
