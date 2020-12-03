from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Zona(models.Model):
    """
        Representan la division de una ciudad en hexagonos
        ej. hay multiples bahias en una zona
    """
    coordenadas = models.PointField(geography=True, default=Point(0.0, 0.0))
