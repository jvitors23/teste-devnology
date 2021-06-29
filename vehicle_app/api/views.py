from django.shortcuts import render
from rest_framework import viewsets, mixins, status

from core.models import Vehicle

from api.serializers import VehicleSerializer

class VehicleViewset(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

