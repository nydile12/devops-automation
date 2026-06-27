import boto3

s3 = boto3.client('s3')
with open('test.txt', 'w') as f:
    f.write("Hello from DevOps Automation")

s3.upload_file(
    "test.txt",
    "devops-automation-nydile",
    "uploaded_test.txt"
)

print("File Uploaded Successfully!")