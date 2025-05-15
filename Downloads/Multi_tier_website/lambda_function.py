import json

def lambda_handler(event, context):
    for record in event['Records']:
        print(f"Received message: {record['body']}")
    return {
        'statusCode': 200,
        'body': json.dumps('SQS message processed successfully')
    }
