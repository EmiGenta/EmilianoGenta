from django.shortcuts import render

# vistas del core
def home(request):
    return render(request, "core/index.html")
