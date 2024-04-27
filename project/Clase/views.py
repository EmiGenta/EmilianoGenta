from django.shortcuts import render, redirect

from . import models, forms

# Creamos el home
def home(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        print(consulta)
        query = models.Comision.objects.filter(nombre__icontains=consulta)
    else:
        query = models.Comision.objects.all()
    context = {"comisiones": query} #consulta a la bdd
    return render(request, "Clase/index.html", context)

def curso_create(request):
    if request.method == "POST":
        form = forms.CursoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("Clase:home")
    else:  # request.method == "GET"
        form = forms.CursoForm()
    return render(request, "Clase/curso_create.html", context={"form": form})