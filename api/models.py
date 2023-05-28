from django.contrib.gis.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    geom = models.PointField()
