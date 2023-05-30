from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance, AsGeoJSON
from api.models import Place


def find_nearest_place(latitude, longitude):
    point = Point(longitude, latitude, srid=4326)

    nearest_place = (
        Place.objects.annotate(distance=Distance("geom", point))
        .annotate(geom_json=AsGeoJSON("geom"))
        .values("id", "name", "geom_json")
        .order_by("distance")
        .first()
    )

    return nearest_place
