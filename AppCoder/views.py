from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


def home(request):
    return render(request, "AppCoder/inicio.html")

# Agregar informacion


def add_alum(request):

    if request.method == 'POST':
        miForm = EstudianteForm(request.POST)

        if miForm.is_valid():

            infoDic = miForm.cleaned_data

            estudiante1 = Estudiante(nombre=infoDic["nombre"],
                                     apellido=infoDic["apellido"],
                                     correo=infoDic["correo"],
                                     ciclo=infoDic["ciclo"])

            estudiante1.save()

            return render(request, "AppCoder/inicio.html")

    else:
        miForm = EstudianteForm()

    return render(request, "AppCoder/add_alum.html", {"form_alumno": miForm})


def add_profe(request):

    if request.method == 'POST':
        miForm = ProfesorForm(request.POST)

        if miForm.is_valid():

            infoDic = miForm.cleaned_data

            profe1 = Profesor(nombre=infoDic["nombre"],
                              apellido=infoDic["apellido"],
                              email=infoDic["email"],
                              profesion=infoDic["profesion"],
                              edad=infoDic["edad"],)

            profe1.save()

            return render(request, "AppCoder/inicio.html")

    else:
        miForm = ProfesorForm()

    return render(request, "AppCoder/add_profe.html", {"form_profe": miForm})


def add_curso(request):

    if request.method == 'POST':
        miForm = CursoForm(request.POST)

        if miForm.is_valid():

            infoDic = miForm.cleaned_data

            curso1 = Curso(nombre=infoDic["nombre"],
                           comision=infoDic["comision"],
                           matriculados=infoDic["matriculados"],)

            curso1.save()

            return render(request, "AppCoder/inicio.html")

    else:
        miForm = CursoForm()

    return render(request, "AppCoder/add_curso.html", {"form_curso": miForm})

# Buscar informacion


def b_alum(request):
    return render(request, "AppCoder/b_alum.html")


def b_profe(request):
    return render(request, "AppCoder/b_profe.html")


def b_curso(request):
    return render(request, "AppCoder/b_curso.html")


# Ver resultados
def r_alum(request):
    """ if request.method == "GET":

        cicloB = request.GET["ciclo"]
        estR = Estudiante.objects.filter(ciclo__icontains=cicloB)

        return render(request, "AppCoder/r_alum.html", {"ciclo": cicloB, "resultado": estR})

    return render(request, "AppCoder/r_alum.html") """

    alumnos = Estudiante.objects.all()
    contexto = {"alumnos": alumnos}

    return render(request, "AppCoder/r_alum.html", contexto)


def r_profe(request):
    if request.method == "GET":

        emailB = request.GET["email"]
        profeR = Profesor.objects.filter(email__icontains=emailB)

        return render(request, "AppCoder/r_profe.html", {"email": emailB, "resultado": profeR})

    return render(request, "AppCoder/r_profe.html")


def r_curso(request):
    if request.method == "GET":

        comisionB = request.GET["comision"]
        cursoR = Curso.objects.filter(comision__icontains=comisionB)

        return render(request, "AppCoder/r_curso.html", {"comision": comisionB, "resultado": cursoR})

    return render(request, "AppCoder/r_curso.html")


# Eliminar

def borrar_alum(request, alumno_nombre):
    alumno_elegido = Estudiante.objects.get(nombre=alumno_nombre)
    alumno_elegido.delete()

    return render(request, "AppCoder/inicio.html")


# Edita

def editar_alum(request, alumno_nombre):
    alumno_elegido = Estudiante.objects.get(nombre=alumno_nombre)

    if request.method == 'POST':
        miForm = EstudianteForm(request.POST)

        if miForm.is_valid():

            infoDic = miForm.cleaned_data

            alumno_elegido.nombre = infoDic["nombre"]
            alumno_elegido.apellido = infoDic["apellido"]
            alumno_elegido.correo = infoDic["correo"]
            alumno_elegido.ciclo = infoDic["ciclo"]

            alumno_elegido.save()

            return render(request, "AppCoder/inicio.html")

    else:
        miForm = EstudianteForm(initial={"nombre": alumno_elegido.nombre,
                                         "apellido": alumno_elegido.apellido,
                                         "correo": alumno_elegido.correo,
                                         "ciclo": alumno_elegido.ciclo})

    return render(request, "AppCoder/edit_alum.html", {"form_alumno": miForm})

# models -


class CursoLista(ListView):
    model = Curso
    template_name = "AppCoder/curso_list.html"


class CursoCrear(CreateView):
    model = Curso
    fields = ["nombre", "comision", "matriculados"]
    # Template se sobreentiende
    success_url = "/AppCoder/cursos/lista"


class CursoBorrar(DeleteView):
    model = Curso
    success_url = "/AppCoder/cursos/lista"


class CursoEditar(UpdateView):
    model = Curso
    fields = ["nombre", "comision", "matriculados"]
    success_url = "/AppCoder/cursos/lista"
