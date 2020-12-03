from django.db import models
from .usuarios import Usuario
from .vehiculos import Vehiculo

class Viaje(models.Model):
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
