import boto3
import json

with open('secrets.json') as f:
        secret = json.load(f)
        
key_id = secret['access_key_id']
access_key = secret['secret_access_key']
bucket = 'grootsbucket'

# session = boto3.Session(profile_name='default')

#Creating Session With Boto3.
session = boto3.Session(aws_access_key_id=key_id, aws_secret_access_key=access_key)
s3 = session.resource('s3')

# txt_data = b'This is the content of the file uploaded from python boto3 asdfasdf'
# object = s3.Object(bucket, 'another_file.txt')
# result = object.put(Body=txt_data)

# res = result.get('ResponseMetadata')
# if res.get('HTTPStatusCode') == 200:
#     print('File Uploaded Successfully')
# else:
#     print('File Not Uploaded')

# result = s3.Bucket(bucket).upload_file('./example_data/pikachu.png','pikachu.png')

result = s3.meta.client.put_object(Body='Text Contents', Bucket=bucket, Key='the_newest_file.txt')
res = result.get('ResponseMetadata')

if res.get('HTTPStatusCode') == 200:
    print('File Uploaded Successfully')
else:
    print('File Not Uploaded')



