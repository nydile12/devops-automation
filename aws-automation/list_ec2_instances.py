import boto3

ec2 = boto3.client('ec2', region_name = 'ap-south-1')
response = ec2.describe_instances()
print("EC2 Instances")
for reservations in response['Reservations']:
    for instances in reservations['Instances']:
        print (f" -> ID {instances['InstanceId']}")
        print (f" Type {instances['InstanceType']}")
        print (f" State {instances['State']['Name']}")

print("Done!")