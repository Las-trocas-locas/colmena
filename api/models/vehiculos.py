from django.db import models

class Vehiculo(models.Model):
    tipo = models.CharField(max_length=30)
    anio = models.IntegerField()
    combustible = models.FloatField()
    capacidad = models.FloatField()
    matricula = models.CharField(max_length=30)
    tag = models.CharField(max_length=30)
    altura = models.FloatField()
    ancho = models.FloatField()
    largo = models.FloatField()
    nombre_dueno = models.CharField(max_length=100)
    tarjeton = models.CharField(max_length=30)
