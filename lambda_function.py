import json


def lambda_handler(event, context):
    return {
        "status": "OK",
        "event": json.dumps(event)
    }
