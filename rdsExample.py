import boto3
import json

with open('secrets.json') as f:
    data = json.load(f)

rds_client = boto3.client('rds',region_name='eu-west-2', aws_access_key_id=data["access_key_id"],
                      aws_secret_access_key=data["access_key"])
response = rds_client.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass='db.t2.micro',
    DBInstanceIdentifier='roys_database_from_python',
    Engine='MySQL',
    MasterUserPassword='testpw0021',
    MasterUsername='admin01',
)

print(response)