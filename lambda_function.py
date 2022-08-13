import json


def lambda_handler(event, context):
    body=json.loads(event["body"])
    broj1=int(body["broj1"])
    broj2=int(body["broj2"])    
    
    return {
        "status": "OK",
        "event": json.dumps(broj1+broj2)
    }
