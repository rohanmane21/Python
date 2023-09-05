import boto3

# b=boto3.resource('s3')
# b.create_bucket(
#     Bucket='rohanrm21',
#     CreateBucketConfiguration={
#         'LocationConstraint': 'ap-south-1',
#     },
# )
# print("Successful uploaded")
# f=open("test.py")
# b.upload_file("test.py","rohanrm21","pem")
# b.download_file("rohanrm21","pem","rm.txt")
# b2=b.Bucket('rohanrm21')

# s3 = boto3.resource("s3")
# for x in s3.buckets.all():
#     print(x.name)

# mb=s3.Bucket('rohanrm21')
# for x in mb.objects.all():
#     print(x.key)

# ec2=boto3.client('ec2')
# instanceid='i-086553d9baf17837a'
# i=ec2.start_instances(
#     InstanceIds=[instanceid])
# if 'StartingInstances' in i:
#         instance_status = i['StartingInstances'][0]['CurrentState']['Name']
#         print(f"Instance {instanceid} is {instance_status}")   

# i=ec2.stop_instances(
#     InstanceIds=[instanceid])
# if i['StoppingInstances'][0]['CurrentState']['Name']== 'stopping':
#     print(f"Instance {instanceid} is Stopped") 

# t=ec2.create_tags(
#     Resources=[
#         'i-086553d9baf17837a'
#     ],
#     Tags = [
#     {'Key': 'Jenk', 'Value': 'Operation'},
# ]
# )
# print(f"Instance Id:{instanceid}")

iam=boto3.client('iam')
# user=iam.create_user(UserName='rock')
# user_arn=user['User']['Arn']
# print(f"user_arn is: {user_arn}")
# g=iam.create_group(GroupName='IAm_Users4')
g=iam.list_groups()
# name=g['Groups']
if 'Groups' in g:
    for x in g['Groups']:
        print(f"{x['GroupName']}")
