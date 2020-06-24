from datetime import timedelta
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from app.models import Alarmclock
from app.serializers import AlarmclockSerializer



# Create your tests here.


class AlarmclockViewSetTestCase(APITestCase):
    def setUp(self) -> None:
        self.get_alarms = []
        for i in range(10):
            db = Alarmclock.objects.create(description=f'test-{i}',
                                           when_will_alarm=timezone.now() + timedelta(seconds=i))
            db.save()
            serialized = AlarmclockSerializer(db).data
            self.get_alarms.append(serialized)

        self.allowed_alarm = {
            "description": "test",
            "when_will_alarm": timezone.now() + timedelta(seconds=10)
        }

        self.alarm_from_past = {
            "description": "from past",
            "when_will_alarm": timezone.now() - timedelta(seconds=10)
        }

        self.alarm_from_past_error = {
            "when_will_alarm": [
                "Unable to set past alarm time"
            ]
        }

    def test_create_alarm(self):
        response = self.client.post(reverse('alarmclock-list'), self.allowed_alarm)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        db = Alarmclock.objects.last()
        serialized_db = AlarmclockSerializer(db).data
        self.assertEqual(response.data, serialized_db)

    def test_get_alarms(self):
        response = self.client.get(reverse('alarmclock-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], self.get_alarms)

    def test_alarm_from_past(self):
        response = self.client.post(reverse('alarmclock-list'), self.alarm_from_past)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, self.alarm_from_past_error)