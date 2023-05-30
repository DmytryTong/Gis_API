from rest_framework import routers
from api.views import PlaceViewSet, find_nearest_place_view
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search-nearby-places/', find_nearest_place_view, name='search-nearby-places'),
]

app_name = "gis"
