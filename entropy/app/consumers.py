import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class AlarmclockConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('alarm_channel', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('alarm_channel', self.channel_name)

    async def alarm(self, event):
        await self.send(text_data=json.dumps(event['message'], ensure_ascii=False))
