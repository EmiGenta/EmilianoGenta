from django.urls import path

from . import views

app_name = 'Clase'

urlpatterns = [
    path('', views.home, name='home'),
    path("curso/create/", views.curso_create, name="curso_create"),
]
