from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from sqs import send_message_sqs


def index(request):
    return render(request, 'sender/server.html')


@csrf_exempt
def receive_message(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            message = data.get("message")
            channel = data.get("channel")
            if message:
                send_message_sqs(json.dumps({'message': message, 'channel': channel}))
                return HttpResponse({"status": "Message sent to queue", "message": message}, status=200)
            else:
                return HttpResponse({"error": "No message provided"}, status=400)
        except json.JSONDecodeError:
            return HttpResponse({"error": "Invalid JSON"}, status=400)
    else:
        return HttpResponse({"error": "Invalid request method"}, status=405)
