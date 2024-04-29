from django.db import models

# Modelos creados
class Curso(models.Model):
    """Definicion de Cursos"""
    nombre = models.CharField(max_length=100)
    cant_max_alumnos = models.PositiveBigIntegerField(default=1000, null=True, blank=True, verbose_name="Cantidad máxima de alumnos")

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "Nombre del Curso"
        verbose_name_plural = "Nombres del Curso"

class Estudiante(models.Model):
    """Definicion de clase Estudiantes"""
    nombre = models.CharField(max_length=200)

    def __str__(self) -> str:
        """Representa una instancia del modelo como una cadena de texto"""
        return self.nombre

class Profesor(models.Model):
    """Definicion de clase Profesores"""
    nombre = models.CharField(max_length=200)

    def __str__(self) -> str:
        """Representa una instancia del modelo como una cadena de texto"""
        return self.nombre
    
class Comision(models.Model):
    """Definicion de Comisiones"""
    nombre = models.PositiveBigIntegerField(unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)
    estudiante = models.ManyToManyField(Estudiante)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        """Representa una instancia del modelo como una cadena de texto"""
        return str(self.nombre)