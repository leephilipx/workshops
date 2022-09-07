import os
import io
import boto3
import json
import csv

# Grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')


# This function contains the main logic of what we want to achieve upon receiving a POST event
def lambda_handler(event, context):
    
    # For debugging purposes
    print("Received event: " + json.dumps(event, indent=2))
    
    # Extract data from POST event
    data = json.loads(json.dumps(event))
    payload = data['data']
    
    # Invoke the sagemaker endpoint with data
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Body=payload)
    
    # Parse the response from endpoint       
    result = json.loads(response['Body'].read().decode())
    pred = int(result)
    labels = ['setosa', 'versicolor', 'virginica']
    
    # Return the results as JSON
    return {
        'data': payload,
        'labels': labels,
        'pred_val': pred,
        'pred_label': labels[pred],
        'status_code': 200
    }