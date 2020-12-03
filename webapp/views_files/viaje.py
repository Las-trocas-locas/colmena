from django.shortcuts import render
from webapp.forms.registro_viaje import RegistroViajeForm
from django.shortcuts import redirect
from api.models.viajes import Viaje
from django.contrib.auth.decorators import login_required
from api.models.vehiculos import Vehiculo

@login_required(login_url='/login/')
def view(request):
    if request.method == 'POST':
        form = RegistroViajeForm(request.POST)
        if form.is_valid():            
            fecha = form.cleaned_data['fecha']
            matricula = form.cleaned_data['matricula_vehiculo']
            try:
                vehiculo = request.user.usuario.vehiculos.filter(matricula=matricula)[0]
            except:
                return render(request, 'crear_viaje.html', {
                    'form': form,
                    'error':"El usuario no tiene registrado un vehículo con esa matrícula"
                })
            viaje = Viaje.objects.create(
                    fecha=fecha,
                    vehiculo=vehiculo,
                    usuario=request.user.usuario
            )
            viaje.save()
            return redirect('/introducir-direcciones/%d' % viaje.pk)
        return render(request, 'crear_viaje.html', {'form': form})
    elif request.method == 'GET':
        form = RegistroViajeForm()
        return render(request, 'crear_viaje.html', {'form': form})
