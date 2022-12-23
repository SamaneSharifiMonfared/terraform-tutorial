import boto3def 

def lambda_handler(event, context):
    result = "Hello World"
    return {
        'statusCode' : 200,
        'body': result
    }


# import os


# def lambda_handler(event, context):
#     return "{} from Lambda!".format(os.environ['greeting'])
