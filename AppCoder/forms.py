from django import forms


class EstudianteForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    ciclo = forms.IntegerField()


class ProfesorForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()
    edad = forms.IntegerField()


class CursoForm(forms.Form):
    nombre = forms.CharField()
    comision = forms.IntegerField()
    matriculados = forms.IntegerField()
