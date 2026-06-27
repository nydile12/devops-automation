import boto3

s3 = boto3.client('s3', region_name = 'ap-south-1')

s3.create_bucket(
    Bucket = 'devops-automation-nydile',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)
print("Bucket created successfully!")