import boto3
import json

user = boto3.client('iam')
def create_policy():
    with open('pipeline4/policy.json', 'r') as f:
        policy_document = json.load(f)
    response = user.create_policy(
        PolicyName="All_Policy",
        PolicyDocument=json.dumps(policy_document) 
    )
def create_user():
    response = iam.create_user(
        UserName='boburao'
    )
    print(response)

create_policy()
