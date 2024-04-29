from django.urls import path

from . import views

app_name = 'Clase'

urlpatterns = [
    path('', views.home, name='home'),
    path('curso_create/', views.curso_create, name='curso_create'),
    path('comision_create/', views.comision_create, name='comision_create'),
    path('curso_list/', views.curso_list, name='curso_list'),  # Nueva URL para la lista de cursos
]
