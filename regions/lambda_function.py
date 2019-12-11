import boto3
import json

def dump_regions():
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions()
    #print(json.dumps(response['Regions']))
    for x in response['Regions']:
        print(x)

def lambda_handler(event, context):
    print(event)
    print(context)
    dump_regions()
