from .tasks import set_alarm
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import Alarmclock
from django.utils import timezone
from .serializers import AlarmclockSerializer


# Create your views here.

alarms = Alarmclock.objects.filter(when_will_alarm__gt=timezone.now()).order_by('when_will_alarm')
for alarm in alarms:
    serializer = AlarmclockSerializer(alarm)
    set_alarm.apply_async(args=(serializer.data,), eta=alarm.when_will_alarm)


class AlarmclockViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Alarmclock.objects.filter(when_will_alarm__gt=timezone.now()).order_by('when_will_alarm')
    serializer_class = AlarmclockSerializer

    def perform_create(self, serializer):
        serializer.save()
        set_alarm.apply_async(args=(serializer.data,),
                              eta=serializer.validated_data['when_will_alarm'])
