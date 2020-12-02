from django.urls import path

from . import views
from .views_files import inicio

urlpatterns = [
    path('', inicio.inicio, name='inicio'),
]
