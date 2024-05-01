from django.urls import path

from . import views

app_name = 'clase'

urlpatterns = [
    path('', views.home, name='home'),
    path('curso/create/', views.curso_create, name='curso_create'),
    path('comision/create/', views.comision_create, name='comision_create'),
    path('curso_list/', views.curso_list, name='curso_list'),
    path('estudiantes/', views.estudiantes_list, name='estudiantes_list'),
    path('profesores/', views.profesores_list, name='profesores_list'),
]
