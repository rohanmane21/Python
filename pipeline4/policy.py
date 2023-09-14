import boto3
import json
user=boto3.client('iam')

response = user.create_policy(
# PolicyName=policy_name,
PolicyDocument=json.loads('policy.json'),
Description='All policy'
)

