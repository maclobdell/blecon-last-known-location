#todo: add license

import boto3, json, os
from datetime import datetime

def lambda_handler(event, context):
    
    body = json.loads(event['body'])

    try: 
        network_headers = body['network_headers']
    except KeyError:
        print("network_headers not found")
        #todo: make sure this works - this is a new addition
        network_headers = []
    try:       
        device_id = network_headers['device_id']
    except KeyError:
        print("device_id not found")
        device_id = None
    else:
        print("device_id: " + device_id)

    try:
        device_location = network_headers['device_location']
    except KeyError:
        print("device_location not found")
        device_location = None
    else:
        print("device_location: " + device_location)

    if device_id != None or device_location != None: 

        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d-%H:%M:%S")
        print("timestamp: " + date_time)


        bucket_name = os.environ.get('S3_BUCKET')

        s3_path = str(device_id) + "/location.json"
        print(s3_path)

        file_content = {'device_id': device_id, 'device_location': device_location, 'timestamp': date_time}

        file_content_string = json.dumps(file_content)

        encoded_string = file_content_string.encode("utf-8")

        upload_to_aws_s3(bucket_name, s3_path, encoded_string)

    dummy_payload = 0    
    body_content = {'response_data': {'payload': str(dummy_payload)}}

    body_length = len(json.dumps(body_content))

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Content-Length': str(body_length)
        },
        'body': json.dumps(body_content)
    }

def upload_to_aws_s3(bucket_name, s3_path, encoded_string):
    s3 = boto3.resource("s3")
    try: 
        s3.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_string)
        print("Message uploaded")
        return True      
    except:
        print("Error uploading message")
        return None
