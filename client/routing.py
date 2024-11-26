from django.urls import re_path

from client import consumer
from django.urls import path

websocket_urlpatterns = [
    re_path(r'^ws/channel1/*.$', consumer.ConsumerChannel1.as_asgi()),  # Define your WebSocket endpoint
    re_path(r'^ws/channel2/*.$', consumer.ConsumerChannel2.as_asgi()),
]