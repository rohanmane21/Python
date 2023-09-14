
import boto3
import json

user = boto3.client('iam')
def attach_policy():
    response = user.attach_user_policy(
    UserName= 'boburao',
    PolicyArn='arn:aws:iam::190616427825:policy/All_Policy'
)
attach_policy()
