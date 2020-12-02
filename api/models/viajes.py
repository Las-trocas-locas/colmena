from django.db import models
from .usuarios import Usuario
from .vehiculos import Vehiculo

class Viaje(models.Model):
    fecha = models.CharField(max_length=30)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)
