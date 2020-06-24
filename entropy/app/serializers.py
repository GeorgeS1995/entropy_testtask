from rest_framework import serializers
from .models import Alarmclock
from django.utils import timezone


class AlarmclockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarmclock
        fields = '__all__'

    def validate_when_will_alarm(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError('Unable to set past alarm time')
        return value
