import json
import boto3
import base64
import os
s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""
    
    # Get the s3 address from the Step Function event input
    key = event['s3_key']
    bucket = event["s3_bucket"]## TODO: fill in
    
    # Download the data from s3 to /tmp/image.png
    ## TODO: fill in
    s3 = boto3.client('s3')
    input_object = '/'.join(key.split('/')[1:])
    file_name = '/tmp/' + os.path.basename(input_object)
    s3.download_file(bucket, key, file_name)
    # We read the data from a file
    with open(file_name, "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }