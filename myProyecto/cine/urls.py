from django.contrib import admin
from django.urls import path,include 
from .views import *

urlpatterns = [
    path('', index,name='IND'),
    path('galeria/',gale,name='GAL'),
    path('formulario/',formulario,name='FORMU'),
    path('quienes_somos/',quienes_somos,name='QUIEN'),
    path('login/',login,name='LOGIN'),
    path('login_acceso/',login_acceso,name='LOGINACCESO'),
    path('cerrar_sesion/',cerrar_sesion,name='CERRARSESION'),
    path('eliminar_pelicula/<id>/',eliminar_pelicula,name='ELIMINA'),
    path('agregar_carrito/<id>/',agregar_carrito,name='AGREGAR'),
    path('listado_flores/',listado_flores,name='listado_flores'),
    path('nueva_flor/',nueva_flor,name="nueva_flor"),
    path('modificar_flores/<id>/',modificar_flores,name="modificar_flores"),
    path('eliminar_flor/<id>/',eliminar_flor,name="eliminar_flor"),
    path('registro_usuario/',registro_usuario, name="registro_usuario"),
]
