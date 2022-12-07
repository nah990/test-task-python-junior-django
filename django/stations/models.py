from django.db import models
from django.utils import timezone
from django.db.models.deletion import SET_NULL
from django.db.models import Sum
import logging

logger = logging.getLogger(__name__)

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
         
            
    def check_condition(self, coordinates):
        logger.info("Checking condition for Station with id = {}".format(self.id))
        if self.condition == self.CONDITION_RUNNING and not all(coordinate > 0 for coordinate in coordinates):
            self.condition = self.CONDITION_BROKEN 
            self.date_breakdown = timezone.now()
            self.save(update_fields=['condition','date_breakdown'])
        logger.info("Condition: {}".format(self.condition))
        
        
    def get_coordinates(self):
        logger.info("Calculating coordinates for Station with id = {}".format(self.id))
        COORDINATE_BY_DEFAULT = 100
        coordinates = dict.fromkeys(("x","y","z"), 0)
        queryset = Pointing.objects.filter(station_id = self.id).values('axis').annotate(coordinate = Sum('distance')).order_by()
        for pair in [{data.pop("axis"):data.pop("coordinate")} for data in queryset]:
            coordinates = coordinates | pair            
        coordinates = [value + COORDINATE_BY_DEFAULT for value in coordinates.values()]
        logger.info("Coordinates: {}".format(', '.join(map(str, coordinates))))
        return coordinates
    
    
class Pointing(models.Model):
    station_id = models.ForeignKey(SpaceStation, on_delete=models.SET_NULL, null=True)
    user = models.TextField()
    POINTING_AXIS_X = 'x'
    POINTING_AXIS_Y = 'y'
    POINTING_AXIS_Z = 'z'
    POINTING_AXIS_CHOICES = [
        (POINTING_AXIS_X, 'x'),
        (POINTING_AXIS_Y, 'y'),
        (POINTING_AXIS_Z, 'z'),
    ]
    axis = models.CharField(
        max_length=1,
        choices=POINTING_AXIS_CHOICES
    )
    distance = models.IntegerField()
    
