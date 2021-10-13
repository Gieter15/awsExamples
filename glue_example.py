import boto3
import json

with open('secrets.json') as f:
    data = json.load(f)

glue_client = boto3.client('glue',region_name='eu-west-2', aws_access_key_id=data["access_key_id"],
                      aws_secret_access_key=data["access_key"])