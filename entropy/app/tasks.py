from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.utils import timezone
from entropy.celery import app
from .models import Alarmclock
from .serializers import AlarmclockSerializer


@app.task()
def set_alarm(alarm):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('alarm_channel', {'type': 'alarm', 'message': alarm})
