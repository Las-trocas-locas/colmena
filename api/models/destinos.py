from django.db import models
from .bahias import Bahia
from .viajes import Viaje
from .areas import Area

class Destinos(models.Model):
    direccion = models.CharField(max_length=30)
    coordenadas = models.CharField(max_length=30)
    llegada_bahia = models.CharField(max_length=30)
    fecha_inicio = models.CharField(max_length=30)
    fecha_termino = models.CharField(max_length=30)
    costo = models.CharField(max_length=30)
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    bahia = models.ForeignKey(Bahia, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
