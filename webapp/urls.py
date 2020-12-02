from django.urls import path

from . import views
from .views_files import inicio, login, registro

urlpatterns = [
    path('', inicio.landing, name='landing'),
    path('login/', login.view, name='login'),
    path('registro/', registro.view, name='registro'),
]
