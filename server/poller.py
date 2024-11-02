import json
import threading
import time

from asgiref.sync import async_to_sync
from schedule import Scheduler

from sqs import receive_messages, delete_messages
from channels.layers import get_channel_layer


def run_continuously(self, interval=1):
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):

        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                self.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.setDaemon(True)
    continuous_thread.start()
    return cease_continuous_run


Scheduler.run_continuously = run_continuously

channel_layer = get_channel_layer()
channels = ['channel1', 'channel2']


def poll_from_sns():
    messages = receive_messages()
    print("polling", messages)
    for message in messages:
        payload = json.loads(message['Body'])
        broadcastTo = payload['channel']
        broadcastMsg = payload['message']
        print('broadcast to', broadcastTo, broadcastMsg)
        if broadcastTo == 'all':
            for channel in channels:
                broadcast(channel, broadcastMsg)
        else:
            broadcast(broadcastTo, broadcastMsg)
        delete_messages(message['ReceiptHandle'])


def broadcast(channel, message):
    async_to_sync(channel_layer.group_send)(
        channel,
        {
            "type": "chat_message",
            "message": message,
        },
    )


def start_scheduler():
    scheduler = Scheduler()
    scheduler.every(2).seconds.do(poll_from_sns)
    scheduler.run_continuously()
