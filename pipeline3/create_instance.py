import boto3

# Get environment variables
import os
AWS_ACCESS_KEY_ID = os.environ.get('AKIASYYM73UYQV2BP2S4')
AWS_SECRET_ACCESS_KEY = os.environ.get('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')
AWS_REGION = os.environ.get('ap-south-1' )
# Create an EC2 client
ec2 = boto3.client('ec2', region_name=AWS_REGION, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Define EC2 instance parameters
instance_params = {
    'ImageId': 'ami-02bb7d8191b50f4bb',  
    'InstanceType': 't2.micro', 
    'KeyName': 'jenkins.pem',  
    'MinCount': 1,
    'MaxCount': 1,
    'TagSpecifications':[
        {
            'ResourceType': 'instance',
            'Tags':[
                {
                    'Key':'Name',
                    'Value':'Ec2_user'
                },
            ]
        },
    ]
}

# Create the EC2 instance
response = ec2.run_instances(**instance_params)

# Print the instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f"EC2 instance created with ID: {instance_id}")

