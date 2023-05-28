from django.shortcuts import render
from rest_framework import viewsets
from api.models import Place
from api.serializers import PlaceSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
