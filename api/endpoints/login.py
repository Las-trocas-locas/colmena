from django.shortcuts import render
from django.http import HttpResponse

def endpoint(request):    
    return render(request, 'login.html', {})


# Create your views here.
