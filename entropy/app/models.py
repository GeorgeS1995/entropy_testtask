from django.db import models

# Create your models here.


class Alarmclock(models.Model):
    description = models.CharField(max_length=1500)
    when_will_alarm = models.DateTimeField()
