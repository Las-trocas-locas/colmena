from django import forms

class RegistroDireccionesForm(forms.Form):

    direccion = forms.CharField(max_length=250)
    longitud = forms.FloatField()
    latitud = forms.FloatField()
