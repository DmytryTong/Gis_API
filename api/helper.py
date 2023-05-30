from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

from api.models import Place


def find_nearest_place(latitude, longitude):
    point = Point(longitude, latitude, srid=4326)

    nearest_place = Place.objects.annotate(distance=Distance('geom', point)).order_by('distance').first()

    return nearest_place

