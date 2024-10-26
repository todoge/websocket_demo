import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ConsumerChannel1(AsyncWebsocketConsumer):
    async def connect(self):
        print("connecting")
        await self.channel_layer.group_add("channel1", self.channel_name)
        await self.accept()
        print("connected")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("channel1", self.channel_name)

    async def chat_message(self, event):
        # Receive message from the group and send it to WebSocket
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))


class ConsumerChannel2(AsyncWebsocketConsumer):
    async def connect(self):
        print("connecting")
        await self.channel_layer.group_add("channel2", self.channel_name)
        await self.accept()
        print("connected")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("channel2", self.channel_name)

    async def chat_message(self, event):
        # Receive message from the group and send it to WebSocket
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
