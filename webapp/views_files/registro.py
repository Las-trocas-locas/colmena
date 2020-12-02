from django.shortcuts import render

def view(request):    
    return render(request, 'inicio/registro.html', {})

# Create your views here.
