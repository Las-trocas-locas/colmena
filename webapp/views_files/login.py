from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from webapp.forms.login import LoginForm
from django.shortcuts import redirect

def view(request):

    if request.method == 'POST':        
        form = LoginForm(request.POST)
        if form.is_valid():            
            correo = form.cleaned_data['correo']
            contrasena = form.cleaned_data['contrasena']
            user = authenticate(username=correo, password=contrasena)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'inicio/login.html', {})
        return render(request, 'inicio/login.html', {'form': form})
    elif request.method == 'GET':
        return render(request, 'inicio/login.html', {})
