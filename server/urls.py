from django.shortcuts import render

# Create your views here.
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("receiver/", views.receive_message, name="receiver"),
]