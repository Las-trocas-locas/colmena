from django import forms

from api.models.usuarios import Usuario

class LoginForm(forms.Form):

    correo = forms.CharField()
    contrasena = forms.CharField()
