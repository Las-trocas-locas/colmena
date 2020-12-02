from django.shortcuts import render

def endpoint(request):    
    return render(request, 'registro.html', {})

# Create your views here.
