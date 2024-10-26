import json

from channels.layers import get_channel_layer
from django.http import HttpResponse
import asyncio

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


async def index(request):
    return render(request, 'receiver/chat.html')


@csrf_exempt
def subscribe(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            message = data.get("group")
            if message:
                return HttpResponse({"status": "Subscribed", "message": "GOOD"}, status=200)
        except json.JSONDecodeError:
            return HttpResponse({"error": "Invalid JSON"}, status=400)
    else:
        return HttpResponse({"error": "Invalid request method"}, status=405)
