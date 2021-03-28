import boto3

client = boto3.client('s3')

BUCKET_NAME = '<S3 BUCKET NAME>'
KEY_NAME = 'index.txt'

response = client.put_object(
    Body='おはようございます',
    Bucket=BUCKET_NAME,
    Key=KEY_NAME,
)
