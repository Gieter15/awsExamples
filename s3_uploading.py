import boto3
import os
import json

folder = 'example_data'
file_name = 'allusers_pipe.txt'
file_path = os.path.join(folder, file_name)

bucket = 'grootsbucket'

with open('secrets.json') as f:
    data = json.load(f)



file_path = os.path.join(folder, file_name)


s3_client = boto3.client('s3', aws_access_key_id=data["access_key_id"],
                      aws_secret_access_key=data["access_key"])
s3_resource = boto3.resource('s3', aws_access_key_id=data["access_key_id"],
                      aws_secret_access_key=data["access_key"])


# bucket_instance = s3_resource.Bucket(name=bucket)
# object_instance = s3_resource.Object(bucket_name=bucket, key="first_file_name")

# object_instance.upload_file("first_file_name")


s3_resource.Object(bucket, file_name).upload_file(Filename=file_path)