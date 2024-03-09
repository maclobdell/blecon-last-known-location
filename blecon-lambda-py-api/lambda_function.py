import json, boto3, os

def lambda_handler(event, context):

    body = json.loads(event['body'])
    device_id = body['device_id']
    bucket_name = os.environ.get('S3_BUCKET')
    s3_path = str(device_id) + "/location.json"

    body_content = download_from_aws_s3(bucket_name, s3_path)
 
    #todo: add error handling - bad connect, bad bucket name, bad object path

    return {
        'statusCode': 200,
        'body': json.dumps(body_content)
    }

def download_from_aws_s3(bucket_name, s3_path):
    
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket_name, Key=s3_path)
    file_content = json.loads(obj['Body'].read())
    return file_content      
