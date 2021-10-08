import boto3
import os
import json

folder = 'example_data'
file_name = 'pikachu.png'
file_path = os.path.join(folder, file_name)

bucket = 'grootsbucket'

with open('secrets.json') as f:
    data = json.load(f)



file_path = os.path.join(folder, file_name)

s3_resource = boto3.resource('s3', aws_access_key_id=data["access_key_id"],
                      aws_secret_access_key=data["access_key"])


s3_client = boto3.client('s3', aws_access_key_id=data["access_key_id"],
                      aws_secret_access_key=data["access_key"])

s3_resource.Object(bucket, 'latest_uploaded_file.png').upload_file(Filename=file_path)