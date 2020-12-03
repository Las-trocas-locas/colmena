from django import forms

from api.models.usuarios import Usuario

class RegistroVehiculoForm(forms.Form):

    tipo = forms.CharField()
    anio = forms.IntegerField()
    combustible = forms.FloatField()
    capacidad = forms.FloatField()
    matricula = forms.CharField()
    tag = forms.CharField()
    altura = forms.FloatField()
    ancho = forms.FloatField()
    largo = forms.FloatField()
    nombre_dueno = forms.CharField()
    tarjeton = forms.CharField()
