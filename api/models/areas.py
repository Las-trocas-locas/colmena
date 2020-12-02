from django.db import models
from .bahias import Bahia

class Area(models.Model):
    """
        Representan las areas de descarga dentro de las bahias
        ej. una bahia tiene muchas areas
    """
    numero = models.CharField(max_length=30)
    bahia = models.ForeignKey(Bahia, on_delete=models.CASCADE)
