# galerias/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('test_template', views.test_template, name="test_template"),
    path('crear_galeria', views.crear_galeria, name="crear_galeria"),
    path('consulta_galerias', views.consulta_galerias, name="consulta_galerias"),
    path('modificar_galeria/<int:pk>', views.modificar_galeria, name="modificar_galeria"),
    path('eliminar_galeria/<int:pk>', views.eliminar_galeria, name="eliminar_galeria"),
    path('crear_cuadro', views.crear_cuadro, name="crear_cuadro"),
    path('consulta_cuadros', views.consulta_cuadros, name="consulta_cuadros"),
    path('modificar_cuadro/<int:pk>', views.modificar_cuadro, name="modificar_cuadro"),
    path('eliminar_cuadro/<int:pk>', views.eliminar_cuadro, name="eliminar_cuadro"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
