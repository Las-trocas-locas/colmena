from django import forms

from api.models.usuarios import Usuario

class RegistroUsuarioForm(forms.Form):

    primer_nombre = forms.CharField()
    segundo_nombre = forms.CharField()
    correo = forms.EmailField()
    contrasena = forms.CharField()
    telefono = forms.CharField()
    licencia = forms.CharField()
