import boto3

client = boto3.client('s3')

BUCKET_NAME = '<S3 BUCKET NAME>'
LAMBDA_ACCESSPINT = '<OBJECT LAMBDA ACCESSPOINT ARN>'
KEY_NAME = 'index.txt'

response = client.get_object(
    Bucket=BUCKET_NAME,
    Key=KEY_NAME,
)

print(response['Body'].read().decode('utf8'))

response = client.get_object(
    Bucket=LAMBDA_ACCESSPINT,
    Key=KEY_NAME,
)

print(response['Body'].read().decode('utf8'))



