from django.db import models

class Zona(models.Model):
    coordenada = models.CharField(max_length=256)    
