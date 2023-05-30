from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.helper import find_nearest_place
from api.models import Place
from api.serializers import PlaceSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


@swagger_auto_schema(
    method="get",
    manual_parameters=[
        openapi.Parameter(
            "latitude",
            openapi.IN_QUERY,
            description="Latitude coordinate of the place",
            type=openapi.TYPE_NUMBER,
            required=True,
        ),
        openapi.Parameter(
            "longitude",
            openapi.IN_QUERY,
            description="Longitude coordinate of the place",
            type=openapi.TYPE_NUMBER,
            required=True,
        ),
    ],
    responses={
        200: "Successful response",
        400: "Invalid latitude or longitude values",
        404: "No nearest place found",
    },
)
@api_view(["GET"])
def find_nearest_place_view(request):
    if request.method == "GET":
        latitude = request.GET.get("latitude")
        longitude = request.GET.get("longitude")

        if latitude is None or longitude is None:
            return Response(
                {"error": "Please provide both latitude and longitude."}, status=400
            )

        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            return Response(
                {"error": "Invalid latitude or longitude values."}, status=400
            )

        nearest_place = find_nearest_place(latitude, longitude)

        if nearest_place is None:
            return Response({"error": "No nearest place found."}, status=404)

        return Response(nearest_place)
