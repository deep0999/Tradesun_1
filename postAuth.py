import json
import boto3
from datetime import datetime
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table( 'userActivityLog')

def lambda_handler(event, context):
    try:
        timestamp = datetime.utcnow().isoformat()
        source = event.get('triggerSource', 'N/A')
        username = event.get('userName', 'N/A')
        raw_json_response = json.dumps(event)

        item = {
            'id': str(uuid.uuid4()),
            'timestamp': timestamp,
            'source': source,
            'username': username,
            'object': raw_json_response
        }

        table.put_item(Item=item)
        print('Data successfully written to DynamoDB')

    except Exception as e:
        print('Error writing to DynamoDB:', e)
        raise

    return event
