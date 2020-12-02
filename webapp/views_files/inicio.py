from django.shortcuts import render
from django.http import HttpResponse


def landing(request):    
    return render(request, 'inicio/landing.html', {})

def login(request):
    return HttpResponse("login")

def registro(request):
    return HttpResponse("registro")
