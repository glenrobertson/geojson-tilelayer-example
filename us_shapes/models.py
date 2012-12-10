from django.contrib.gis.db import models


class US_State(models.Model):
    sub_region = models.CharField(max_length=80)
    state_name = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
