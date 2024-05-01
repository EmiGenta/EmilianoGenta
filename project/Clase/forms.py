from django import forms
from . import models
from .models import Curso, Profesor

class CursoForm(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "cant_max_alumnos": forms.TextInput(attrs={"class": "form-control"}),
        }

class ComisionForm(forms.ModelForm):
    class Meta:
        model = models.Comision
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "curso": forms.Select(attrs={"class": "form-control"}),
            "estudiante": forms.SelectMultiple(attrs={"class": "form-control"}),
            "profesor": forms.Select(attrs={"class": "form-control"}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Obtener las opciones disponibles para el campo "curso"
        cursos = Curso.objects.all()
        # Obtener las opciones disponibles para el campo "profesor"
        profesores = Profesor.objects.all()
        # Asignar las opciones al widget correspondiente
        self.fields["curso"].queryset = cursos
        self.fields["profesor"].queryset = profesores

