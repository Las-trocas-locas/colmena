from django import forms

from api.models.viajes import Viaje

class RegistroViajeForm(forms.Form):

    fecha = forms.DateField()    
    matricula_vehiculo = forms.CharField()
