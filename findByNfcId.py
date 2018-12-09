import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello World, how are you? today is 12-07-18',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
