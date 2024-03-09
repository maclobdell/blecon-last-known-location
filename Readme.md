# API to Get Last Known Location of a Blecon Tracker
By Mac Lobdell

If you have the device_id of the tracker, you can get its last known location using this simple API.

It is based on API gateway, lambdas, and S3 only, so it is serverless and should be cheap. 


# Parts

## blecon-lambda-py

This is the lambda that receives notifications (device requests,etc) from the blecon network.
Setup an API Gateway with an Rest API that is Open.
Copy the API to the Blecon console Request Handlers. 

This saves the device_id and location to a file in the specified S3 bucket.

Note that the boto3 python library is used to be able to read/write to S3. This causes the lambda package size to be over the limit for viewing and editing within the console. So you have to zip it up and upload it.

The procedure for zipping and uploading goals like this.


First setup the dependencies.

Create a file called requirements.txt and add a single line with 'boto3'

boto3

Then run this command to install the requirements to a folder within the local directory.

pip install -r requirements.txt --target ./package

When you are done creating your lambda function, you want to zip up just the critical stuff and not the python cache or other files so do this.

'''
cd package 
zip -r ../blecon-lambda-py.zip .
cd .. 
zip -g blecon-lambda-py.zip lambda_function.py
'''

Run this to set the environment variable locally for the S3 bucket name

export S3_BUCKET="<name of s3 bucket>"

In Lambda set an environment variable for this in the console. 


## blecon-lambda-py-api

This lambda will recieve requests you make from any application you create like a desktop, web, or mobile app.

You need to send a request to it that looks like this.

    request_data = {'device_id':'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx'}
    header_data =  {'Content-Type': 'application/json'}

    r = requests.post('https://xxxxxxxxxx.execute-api.us-east-2.amazonaws.com/default/blecon-locator-api', headers=header_data, json=request_data)


It will then return something like this.

{'device_id': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx', 'device_location': '50.xxxxxxxxxxxxxxxx,0.xxxxxxxxxxxxxxxx', 'timestamp': '09_23_2022_18_34_41'}

The timestamp is in a format I made up, which I need to set it to the standard way timestamps get sent over the web.  


# Tests

  The api-test.py works. It will make an appropriate request. 

  the local-test.py in the blecon-lambda-py also works. 

  the local-test.py in the blecon-lambda-py-api DOES NOT WORK. I think there is a problem with how I'm passing it data to simulate an event. 

  api-test-test.py is a test of a separate API that was mocked for debugging purposes.
