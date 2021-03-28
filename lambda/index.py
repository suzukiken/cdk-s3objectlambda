import boto3
import urllib.request

def lambda_handler(event, context):
    print(event)
    print(boto3.__version__)
    
    object_get_context = event["getObjectContext"]
    request_route = object_get_context["outputRoute"]
    request_token = object_get_context["outputToken"]
    s3_url = object_get_context["inputS3Url"]

    opened = urllib.request.urlopen(s3_url)
    source = opened.read().decode('utf-8')
    print(source)
    response_body = 'どうも{}'.format(source)

    s3 = boto3.client('s3')
    s3.write_get_object_response(
        Body=response_body,
        RequestRoute=request_route,
        RequestToken=request_token)
    
    return {'status_code': 200}