from django.urls import path
from .views import *

urlpatterns = [ 
    path('', indexView, name = 'index'),
    path('mostrar/',lista_laboratorios , name = 'lista_laboratorios'),
    path('editar/<int:laboratorio_id>/', editar_laboratorio, name='editar_laboratorio'),
    path('eliminar/<int:laboratorio_id>/', eliminar_laboratorio, name='eliminar_laboratorio'),
    path('agregar/',crear_laboratorio , name = 'crear_laboratorio'),
]
