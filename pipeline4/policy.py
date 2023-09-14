import boto3
import json
user=boto3.client('iam')

response = user.create_policy(
PolicyName='All_Policy',
f = open('policy.json')
PolicyDocument = json.load(f)
# =json.loads('policy.json'),
Description='All policy'
)

