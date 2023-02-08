from django.urls import path
from AppCoder import views 

urlpatterns = [
    path('',views.inicio, name="Inicio"), #Esta era nuestra primera vista
    path('cursos/',views.cursos, name="Cursos"),
    path('profesores/',views.profesores, name="Profesores"),
    path('estudiantes/',views.estudiantes, name="Estudiantes"),
    path('entregables/',views.entregrables, name="Entregables"),
]