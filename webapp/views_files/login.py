from django.shortcuts import render
from django.http import HttpResponse

def view(request):    
    return render(request, 'inicio/login.html', {})


# Create your views here.
