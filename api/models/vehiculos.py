from django.db import models

class Vehiculo(models.Model):
    tipo = models.CharField(max_length=30)
    anio = models.CharField(max_length=30)
    combustible = models.CharField(max_length=30)
    capacidad = models.CharField(max_length=30)
    matricula = models.CharField(max_length=30)
    tag = models.CharField(max_length=30)
    dimensiones = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    tarjeton = models.CharField(max_length=30)
