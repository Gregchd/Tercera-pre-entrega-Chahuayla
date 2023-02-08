from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=254)
    ciclo = models.IntegerField(default=0)


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    profesion = models.CharField(max_length=50)
    edad = models.IntegerField(default=0)


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    matriculados = models.IntegerField(default=0)
