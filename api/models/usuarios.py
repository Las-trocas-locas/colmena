from django.db import models
from .vehiculos import Vehiculo
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=30)
    licencia = models.CharField(max_length=30)
    vehiculos = models.ManyToManyField(Vehiculo)
