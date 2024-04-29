from django import forms

from . import models

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
            "curso": forms.TextInput(attrs={"class": "form-control"}),
            "estudiante": forms.TextInput(attrs={"class": "form-control"}),
            "profesor": forms.TextInput(attrs={"class": "form-control"}),
        }

class CursoFormNew(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = "__all__"
