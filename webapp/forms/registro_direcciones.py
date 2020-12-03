from django import forms

class RegistroDireccionesForm(forms.Form):

    direccion = forms.CharField()
