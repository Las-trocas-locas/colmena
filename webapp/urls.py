from django.urls import path

from . import views
from .views_files import inicio, login, registro, registro_vehiculos, viaje, direcciones

urlpatterns = [
    path('', inicio.landing, name='landing'),
    path('login/', login.view, name='login'),
    path('registro/', registro.view, name='registro'),
    path('registro-vehiculo/', registro_vehiculos.view, name='registro-vehiculo'),
    path('crear-viaje/', viaje.view, name='crear-viaje'),
    path('introducir-direcciones/<int:viaje_pk>', direcciones.view, name='introducir-direcciones')
]
