from django.shortcuts import render

def view(request):    
    return render(request, 'registro.html', {})

# Create your views here.
