from datetime import timedelta
import pytest
from channels.testing import WebsocketCommunicator
from django.utils import timezone
from entropy.routing import application
from app.tasks import set_alarm
from app.serializers import AlarmclockSerializer
from channels.db import database_sync_to_async

allowed_alarm = {
    "description": "test",
    "when_will_alarm": timezone.now() + timedelta(seconds=5)
}

@database_sync_to_async
def create_alarm():
    serializer = AlarmclockSerializer(data=allowed_alarm)
    serializer.is_valid()
    set_alarm.apply_async(args=(serializer.data,),
                          eta=serializer.validated_data['when_will_alarm'])
    return serializer

@pytest.mark.asyncio
async def test_alarm():
    communicator = WebsocketCommunicator(application, "ws/alarm/")
    connected, _ = await communicator.connect()
    assert connected
    serializer = await create_alarm()
    response = await communicator.receive_json_from(timeout=6.0)
    assert response == serializer.data


