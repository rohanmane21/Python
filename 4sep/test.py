import boto3
import json
from datetime import datetime

ec2= boto3.client('ec2')

new_instance ={
    "ImageId": "ami-06f621d90fa29f6d0",
    "MinCount":1,
    "MaxCount":1,
    "InstanceType":"t2.micro",
    "KeyName":"bunny",
    'TagSpecifications':[
        {
            'ResourceType': 'instance',
            'Tags':[
                {
                    'Key':'Name',
                    'Value':'babu'
                },
            ]
        },
    ]
    }
response = ec2.run_instances(**new_instance)
def convert_datetime_to_string(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
# Load the JSON configuration file
jsonfile='ec2_instance_config.json'
with open(jsonfile, 'w') as config_file:
    config_data = json.dump(response,config_file,indent=4,default=convert_datetime_to_string)

# # Create an EC2 client
# ec2_client = boto3.resource('ec2', region_name='ap-south-1a')
# ec2_client.create_instances(**config_data)

# # Create the EC2 instance

# # Extract the instance ID
# instance_id = response['Instances'][0]['InstanceId']

# print(f"EC2 instance {instance_id} created successfully.")

# import boto3
# import json 
# ec2=boto3.resource('ec2')
# def create_instance():
#     with open('ec2.json', 'r') as f:
#         cf = f.read()
#         config_data = json.dumps(cf)
#         ec2.create_instances(config_data)
# create_instance()

# i=ec2.start_instances(
#     InstanceIds=[instanceid])
# if 'StartingInstances' in i:
#         instance_status = i['StartingInstances'][0]['CurrentState']['Name']
#         print(f"Instance {instanceid} is {instance_status}")   
