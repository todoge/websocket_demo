# queue_app/sqs.py
import boto3
from botocore.exceptions import ClientError


# def get_secret():
#
#     secret_name = "websocket_demo"
#     region_name = "ap-southeast-1"
#
#     # Create a Secrets Manager client
#     session = boto3.session.Session()
#     client = session.client(
#         service_name='secretsmanager',
#         region_name=region_name
#     )
#
#     try:
#         get_secret_value_response = client.get_secret_value(
#             SecretId=secret_name
#         )
#     except ClientError as e:
#         # For a list of exceptions thrown, see
#         # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
#         raise e
#
#     secret = get_secret_value_response['SecretString']
#
# print('secret', get_secret())

sqs = boto3.client('sqs')
queue_url="https://sqs.ap-southeast-1.amazonaws.com/048708096523/websocketDemo"


def send_message_sqs(message_body):
    """Send a message to the specified SQS queue."""
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body
    )
    return response['MessageId']

def receive_messages():
    """Receive messages from the specified SQS queue."""
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10,  # Adjust based on your needs
        WaitTimeSeconds=0  # Long polling
    )
    return response.get('Messages', [])
def delete_messages(receipt_handle):
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )

