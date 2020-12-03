from django.shortcuts import render
from django.shortcuts import redirect
from api.models.viajes import Viaje
from api.models.destinos import Destino
from api.models.bahias import Bahia
from webapp.forms.registro_direcciones import RegistroDireccionesForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.gis.geos import Point
#from django.contrib.gis.measure import Distance
from django.contrib.gis.db.models.functions import Distance

@login_required(login_url='/login/')
def view(request, viaje_pk):
    viaje = get_object_or_404(Viaje, pk=viaje_pk)
    if viaje.usuario.pk != request.user.usuario.pk:
        raise Http404("No existe ese viaje.")
    if request.method == 'POST':
        form = RegistroDireccionesForm(request.POST)
        error = ""
        if form.is_valid():
            direccion = form.cleaned_data['direccion']
            longitud = form.cleaned_data['longitud']
            latitud = form.cleaned_data['latitud']
            punto = Point(longitud, latitud)
            bahias = Bahia.objects.filter(
                coordenadas__dwithin=(
                    punto,
                    100000
                )
            ).annotate(distance=Distance('coordenadas', punto)).order_by('distance')
            if bahias.count() > 0:
                bahia = bahias[0]
                destino = Destino.objects.create(direccion=direccion,
                                                 coordenadas=punto,
                                                 bahia=bahia,
                                                 area=bahia.area_set.all()[0],
                                                 viaje=viaje
                                                 )
                destino.save()
            else:
                error = "No hay ninguna bahía cercana al destino"
        direcciones = viaje.destino_set.all()
        return render(request, 'registrar_direcciones.html', {'form': form,
                                                              'direcciones': direcciones,
                                                              'error': error
                                                              })
    elif request.method == 'GET':
        form = RegistroDireccionesForm()
        direcciones = viaje.destino_set.all()
        return render(request, 'registrar_direcciones.html', {'form': form,
                                                              'direcciones': direcciones})
