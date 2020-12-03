from django.shortcuts import render
from webapp.forms.registro_vehiculo import RegistroVehiculoForm
from django.shortcuts import redirect
from api.models.vehiculos import Vehiculo
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def view(request):
    if request.method == 'POST':
        form = RegistroVehiculoForm(request.POST)
        if form.is_valid():            
            tipo = form.cleaned_data['tipo']
            anio = form.cleaned_data['anio']
            combustible = form.cleaned_data['combustible']
            capacidad = form.cleaned_data['capacidad']
            matricula = form.cleaned_data['matricula']
            tag = form.cleaned_data['tag']
            altura = form.cleaned_data['altura']
            ancho = form.cleaned_data['ancho']
            largo = form.cleaned_data['largo']
            nombre_dueno = form.cleaned_data['nombre_dueno']
            tarjeton = form.cleaned_data['tarjeton']
            vehiculo = Vehiculo.objects.create(
                tipo = tipo,
                anio = anio,
                combustible = combustible,
                capacidad = capacidad,
                matricula = matricula,
                tag = tipo,
                altura = altura,
                ancho = ancho,
                largo = largo,
                nombre_dueno = nombre_dueno,
                tarjeton = tarjeton                
            )
            vehiculo.save()
            request.user.usuario.vehiculos.add(vehiculo)            
            return redirect('/')
        return render(request, 'inicio/registro_vehiculo.html', {'form': form})
    elif request.method == 'GET':
        form = RegistroVehiculoForm()
        return render(request, 'inicio/registro_vehiculo.html', {'form': form})
