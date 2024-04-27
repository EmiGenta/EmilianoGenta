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