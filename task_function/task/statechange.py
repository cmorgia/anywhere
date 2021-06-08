from schema.aws.ecs.ecstaskstatechange import Marshaller
from schema.aws.ecs.ecstaskstatechange import AWSEvent
from schema.aws.ecs.ecstaskstatechange import ECSTaskStateChange
import json
import boto3

def findTargetGroup(cluster,taskDef):
    client = boto3.client('ecs')
    paginator = client.get_paginator('list_services').paginate(
        cluster=cluster
    )
    targetGroup=None
    for srvArn in paginator:
        srv = client.describe_services(cluster=cluster,services=[srvArn['serviceArns'][0]])['services'][0]
        if srv['taskDefinition']==taskDef:
            response = client.list_tags_for_resource(
                resourceArn=srv['serviceArn']
            )
            
            for tag in response['tags']:
                if (tag['key']=='targetGroup'):
                    targetGroup = tag['value']

    return targetGroup

def findIpAddress(cluster,containerInstanceArn):
    client = boto3.client('ecs')
    ec2InstanceId = client.describe_container_instances(cluster=cluster,containerInstances=[containerInstanceArn])['containerInstances'][0]['ec2InstanceId']
    
    client = boto3.client('ssm')
    ipAddress = client.describe_instance_information(
        Filters=[
            {
                'Key': 'InstanceIds',
                'Values': [
                    ec2InstanceId
                ]
            },
        ]
    )['InstanceInformationList'][0]['IPAddress']

    return ipAddress

def lambda_handler(event, context):
    """Sample Lambda function reacting to EventBridge events

    Parameters
    ----------
    event: dict, required
        Event Bridge Events Format

        Event doc: https://docs.aws.amazon.com/eventbridge/latest/userguide/event-types.html

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
        The same input event file
    """

    #Deserialize event into strongly typed object
    awsEvent:AWSEvent = Marshaller.unmarshall(event, AWSEvent)
    detail:ECSTaskStateChange = awsEvent.detail
    cluster = detail.clusterArn
    taskDef = detail.taskDefinitionArn
    containerInstanceArn = detail.containerInstanceArn

    targetGroup = findTargetGroup(cluster,taskDef)
    print("Target group="+targetGroup)

    ipAddress = findIpAddress(cluster,containerInstanceArn)
    print("IP Address="+ipAddress)

    print('Looping through containers')
    client = boto3.client('elbv2')
    for container in awsEvent.detail.containers:
        for binding in container.networkBindings:
            if (binding.bindIP=='0.0.0.0'):
                port = int(binding.hostPort)

                if (detail.desiredStatus=='RUNNING'):
                    print("Register target IP {} with port {}".format(ipAddress,port))
                    client.register_targets(
                        TargetGroupArn=targetGroup,
                        Targets=[
                            {
                                'Id': ipAddress,
                                'Port': port,
                                'AvailabilityZone': 'all'
                            }
                        ]
                    )
                else:
                    print("Deregister target IP {} with port {}".format(ipAddress,port))
                    client.deregister_targets(
                        TargetGroupArn=targetGroup,
                        Targets=[
                            {
                                'Id': ipAddress,
                                'Port': port,
                                'AvailabilityZone': 'all'
                            }
                        ]
                    )

    #Return event for further processing
    return Marshaller.marshall(awsEvent)
