from django.shortcuts import render
from django.shortcuts import redirect
from api.models.viajes import Viaje
from api.models.vehiculos import Vehiculo
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import Http404

@login_required(login_url='/login/')
def view(request, viaje_pk):
    viaje = get_object_or_404(Viaje, pk=viaje_pk)
    if viaje.usuario.pk != request.user.usuario.pk:
        raise Http404("No existe ese viaje.")        
    if request.method == 'POST':
        form = RegistroViajeForm()
        return render(request, 'registrar_direcciones.html', {'form': form})
    elif request.method == 'GET':
        form = RegistroViajeForm()
        return render(request, 'registrar_direcciones.html', {'form': form})
