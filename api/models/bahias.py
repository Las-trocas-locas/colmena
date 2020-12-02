from django.db import models
from .zonas import Zona

class Bahia(models.Model):
    direccion = models.CharField(max_length=30)
    coordenadas = models.CharField(max_length=30)
    fecha_alta = models.CharField(max_length=30)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
