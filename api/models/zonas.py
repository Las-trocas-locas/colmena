from django.db import models

class Zona(models.Model):
    """
        Representan la division de una ciudad en hexagonos
        ej. hay multiples bahias en una zona
    """
    coordenada = models.CharField(max_length=256)    
