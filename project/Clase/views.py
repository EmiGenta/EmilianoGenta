from django.shortcuts import render

from . import models

# Creamos el home
def home(request):
    query = models.Comision.objects.all()
    context = {"comisiones": query} #consulta a la bdd
    return render(request, "Clase/index.html", context)