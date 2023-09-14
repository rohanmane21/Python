import boto3
import json

user = boto3.client('iam')
with open('policy.json', 'r') as f:
    policy_document = json.load(f)
response = user.create_policy(
    PolicyName="All_P",
    PolicyDocument=json.dumps(policy_document) 
)
