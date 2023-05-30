from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.helper import find_nearest_place
from api.models import Place
from api.serializers import PlaceSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


@api_view(['GET'])
def find_nearest_place_view(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')

    if latitude is None or longitude is None:
        return Response({'error': 'Please provide both latitude and longitude.'}, status=400)

    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        return Response({'error': 'Invalid latitude or longitude values.'}, status=400)

    nearest_place = find_nearest_place(latitude, longitude)

    if nearest_place is None:
        return Response({'error': 'No nearest place found.'}, status=404)

    serialized_place = {
        'id': nearest_place.id,
        'name': nearest_place.name,
        'description': nearest_place.description,
        'distance': nearest_place.distance.m
    }

    return Response(serialized_place)
