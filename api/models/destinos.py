#from django.db import models
from .bahias import Bahia
from .viajes import Viaje
from .areas import Area
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Destino(models.Model):
    direccion = models.CharField(max_length=250)
    coordenadas = models.PointField(geography=True, default=Point(0.0, 0.0))
    llegada_bahia = models.DateTimeField()
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    costo = models.FloatField()
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    bahia = models.ForeignKey(Bahia, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
