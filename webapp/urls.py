from django.urls import path

from . import views
from .views_files import inicio

urlpatterns = [
    path('', inicio.landing, name='landing'),
    path('login/', inicio.login, name='login'),
    path('registro/', inicio.registro, name='registro'),
]
