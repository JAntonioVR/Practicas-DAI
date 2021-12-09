# galerias/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test_template', views.test_template, name="test_template"),
    path('crear_galeria', views.crear_galeria, name="crear_galeria"),
    path('consulta_galerias', views.consulta_galerias, name="consulta_galerias"),
    path('modificar_galeria/<int:pk>', views.modificar_galeria, name="modificar_galeria"),
    path('eliminar_galeria/<int:pk>', views.eliminar_galeria, name="eliminar_galeria"),
    
]