import boto3
ddb = boto3.client("dynamodb")

def handler(event, context):
    try:
        data = ddb.scan(
            TableName="BTMenu"
        )
        print(data)
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
