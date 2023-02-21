from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('home/', home, name="home"),
    path('agregar_alumno/', add_alum, name="a_alumno"),
    path('agregar_profe', add_profe, name="a_profe"),
    path('agregar_curso', add_curso, name="a_curso"),
    path('buscar_alumno/', b_alum, name="b_alumno"),
    path('buscar_profe', b_profe, name="b_profe"),
    path('buscar_curso', b_curso, name="b_curso"),
    path('r_alumno/', r_alum, name="r_alumno"),
    path('r_profe/', r_profe, name="r_profe"),
    path('r_curso/', r_curso, name="r_curso"),
    # borrar
    path('borrar_alum/<alumno_nombre>/', borrar_alum, name="Borrar_alum"),

    # editar
    path('edit_alum/<alumno_nombre>/', editar_alum, name="editar_alum"),
]
