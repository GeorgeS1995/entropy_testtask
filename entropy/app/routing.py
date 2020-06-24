from django.urls import path
from .consumers import AlarmclockConsumer

websocket = [
    path('ws/alarm/', AlarmclockConsumer)
]