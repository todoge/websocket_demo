# queue_app/sqs.py
import boto3
from botocore.exceptions import ClientError

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

