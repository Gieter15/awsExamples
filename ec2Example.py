import boto3
import os
import json

# boto3.Session(profile_name='default')

with open('secrets.json') as f:
        secret = json.load(f)
        
key_id = secret['access_key_id']
access_key = secret['secret_access_key']
bucket = 'grootsbucket'

# os.environ['AWS_PROFILE'] = 'MyProfile'
# os.environ['AWS_DEFAULT_REGION'] = 'eu-west-2'

session = boto3.Session(aws_access_key_id=key_id, aws_secret_access_key=access_key)
ec2_client = session.client('ec2')

response = ec2_client.describe_regions()
print(response['Regions'])