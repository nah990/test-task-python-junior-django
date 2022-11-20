from django.db import models
from django.utils import timezone
from django.db.models.deletion import SET_NULL


class SpaceStation(models.Model):
    name = models.TextField(null=True)
    CONDITION_RUNNING = 'running'
    CONDITION_BROKEN = 'broken'
    CONDITION_CHOICES = [
        (CONDITION_RUNNING, 'running'),
        (CONDITION_BROKEN, 'broken'),
    ]
    condition = models.CharField(
        max_length=7,
        choices=CONDITION_CHOICES,
        default=CONDITION_RUNNING)
    date_created = models.DateTimeField(default=timezone.now)
    date_breakdown = models.DateTimeField(null=True)


class Pointing(models.Model):
    station_id = models.ForeignKey(SpaceStation, on_delete=models.SET_NULL, null=True)
    user = models.TextField()
    axis = models.TextField()
    distance = models.IntegerField()