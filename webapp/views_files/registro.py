from django.shortcuts import render
from webapp.forms.registro_usuario import RegistroUsuarioForm
from django.shortcuts import redirect
from api.models.usuarios import Usuario
from django.contrib.auth.models import User

def view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():            
            primer_nombre = form.cleaned_data['primer_nombre']
            segundo_nombre = form.cleaned_data['segundo_nombre']
            correo = form.cleaned_data['correo']
            contrasena = form.cleaned_data['contrasena']
            telefono = form.cleaned_data['telefono']
            licencia = form.cleaned_data['licencia']
            user = User.objects.create_user(
                username=correo,
                first_name=primer_nombre,
                last_name=segundo_nombre,
                email=correo,
                password=contrasena)
            user.save()
            usuario = Usuario.objects.create(
                user=user,
                telefono=telefono,
                licencia=licencia
            )
            usuario.save()
            return redirect('/login')
        return render(request, 'inicio/registro.html', {'form': form})
    elif request.method == 'GET':
        form = RegistroUsuarioForm()
        return render(request, 'inicio/registro.html', {'form': form})

# Create your views here.
