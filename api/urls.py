from django.urls import path

from . import views
# los endpoints van en archivos separados
from . import endpoints

urlpatterns = [
    path('login', endpoints.login, name='login'),
    path('registro', endpoints.registro, name='registro')
]
