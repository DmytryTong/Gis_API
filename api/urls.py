from django.urls import include, path
from rest_framework import routers
from api.views import PlaceViewSet

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

app_name = "gis"
