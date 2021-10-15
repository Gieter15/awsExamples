import boto3
import os
import json

os.environ['AWS_PROFILE'] = 'MyProfile'
os.environ['AWS_DEFAULT_REGION'] = 'eu-west-2'

crawler_name = 'roys_crawler'

with open('secrets.json') as f:
    data = json.load(f)

glue_client = boto3.client('glue',region_name='eu-west-2')
glue_client.start_crawler(name=crawler_name)
