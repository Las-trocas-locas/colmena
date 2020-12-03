#from django.db import models
from .zonas import Zona
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Bahia(models.Model):
    direccion = models.CharField(max_length=250)
    coordenadas = models.PointField(geography=True, default=Point(0.0, 0.0))
    fecha_alta = models.DateTimeField()
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
