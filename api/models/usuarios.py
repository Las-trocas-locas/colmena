from django.db import models
from .vehiculos import Vehiculo

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    licencia = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    vehiculos = models.ManyToManyField(Vehiculo)