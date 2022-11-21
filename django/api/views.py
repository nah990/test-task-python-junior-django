from django.shortcuts import render
from django.http import Http404
from stations.models import SpaceStation, Pointing
from .serializers import SpaceStationSerializer, PointingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.db.models import Sum
# Create your views here.

#generic class-based views (?)
class SpaceStationList(APIView):
    def get(self, request):
        stations = SpaceStation.objects.all()
        serializer = SpaceStationSerializer(stations, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = SpaceStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SpaceStationDetail(APIView):
    def get_object(self, pk):
        try:
            return SpaceStation.objects.get(pk=pk)
        except SpaceStation.DoesNotExist:
            raise Http404
    
    
    def get(self, request, pk, format=None):
        station = self.get_object(pk)
        serializer = SpaceStationSerializer(station)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        station = self.get_object(pk)
        serializer = SpaceStationSerializer(station, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def patch(self, request, pk):
        station = self.get_object(pk)
        serializer = SpaceStationSerializer(station, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        station = self.get_object(pk)
        station.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class SpaceStationState(APIView):
    def get_object(self, pk):
        try:
            return SpaceStation.objects.get(pk=pk)
        except SpaceStation.DoesNotExist:
            raise Http404
         
         
    def get(self, request, pk):
        station = self.get_object(pk)
        coordinates = station.get_coordinates()
        return Response(coordinates)
        
        
    def post(self, request, pk):
        station = self.get_object(pk)
        serializer = PointingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        coordinates = station.get_coordinates()
        
        return Response(coordinates, status=status.HTTP_201_CREATED)