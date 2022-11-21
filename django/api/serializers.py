from rest_framework import serializers
from stations.models import SpaceStation, Pointing

class SpaceStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceStation
        fields = '__all__'


class PointingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pointing
        fields = '__all__'
    
