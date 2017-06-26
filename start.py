from __future__ import print_function
import boto3
import os

print('Loading function')

# Enter the region your instances are in, e.g. 'us-east-1'
REGION = os.getenv('REGION')

# Enter key, value of tagged EC2 instaces
TAGKEY, TAGVALUE = os.getenv('TAGKEY'), os.getenv('TAGVALUE')
 

def lambda_handler(event, context):

    ec2client = boto3.client('ec2', region_name=REGION)

    # get tagged instances
    response = ec2client.describe_instances(Filters=[{'Name': 'tag:'+TAGKEY, 'Values': [TAGVALUE]},
                                                     {'Name': 'instance-state-name', 'Values': ['stopped']}])

    instancelist = []
    for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            instancelist.append(instance["InstanceId"])

    # start instances
    ec2client.start_instances(InstanceIds=instancelist)
    print('started instances: ' + str(instancelist))

    return 'success'
