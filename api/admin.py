from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models.zona import Zona
from .models.usuarios import Usuario
from .models.bahias import Bahia
from .models.areas import Area #zonas_bahía
from .models.vehiculos import Vehiculo
from .models.destinos import Destino
from .models.viajes import Viaje


admin.site.register(Usuario)
admin.site.register(Zona)
admin.site.register(Bahia)
admin.site.register(Area)
admin.site.register(Vehiculo)
admin.site.register(Destino)
admin.site.register(Viaje)
