import json
import base64
import os
import io
import boto3


# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2023-01-28-13-26-00-997'## TODO: fill in
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['image_data'])

    # Instantiate a Predictor


    # For this model the IdentitySerializer needs to be "image/png"
    
    
    # Make a prediction:
    inference = runtime.invoke_endpoint(EndpointName=ENDPOINT,
                                       ContentType='application/x-image',
                                       Body=image)
    
    # We return the data back to the Step Function 
    result = inference["Body"].read().decode()
    result_json = json.loads(result)
    event["inferences"] = result_json
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }