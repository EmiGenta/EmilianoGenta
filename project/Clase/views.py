from django.shortcuts import render, redirect
from . import models, forms
from .models import Curso, Comision, Estudiante, Profesor

# Creamos el home
def home(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        print(consulta)
        query = models.Comision.objects.filter(nombre__icontains=consulta)
    else:
        query = models.Comision.objects.all()
    context = {"comisiones": query} #consulta a la bdd
    return render(request, "clase/index.html", context)

def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'clase/curso_list.html', {'cursos': cursos})

def curso_create(request):
    if request.method == "POST":
        form = forms.CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clase:curso_list")
    else:  # request.method == "GET"
        form = forms.CursoForm()
    return render(request, "clase/curso_create.html", {"form": form})

def comision_create(request):
    if request.method == "POST":
        form = forms.ComisionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clase:home")
    else:  # request.method == "GET"
        form = forms.ComisionForm()
    return render(request, "clase/comision_create.html", context={"form": form})

# def estudiantes_list(request):
#     estudiantes = Estudiante.objects.all()
#     return render(request, 'Clase/estudiantes_list.html', {'estudiantes': estudiantes})

def estudiantes_list(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        estudiantes = Estudiante.objects.filter(nombre__icontains=consulta)
    else:
        estudiantes = Estudiante.objects.all()
    return render(request, 'clase/estudiantes_list.html', context={'estudiantes': estudiantes})

def profesores_list(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        profesores = Profesor.objects.filter(nombre__icontains=consulta)
    else:
        profesores = Profesor.objects.all()
    return render(request, 'clase/profesores_list.html', context={'profesores': profesores})