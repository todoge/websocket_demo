from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Welcome to the websocket demo. This is the client page")