# galerias/models.py
from django.db import models
from django.utils import timezone
from django.forms import ModelForm

  
class Galeria(models.Model):
    nombre     = models.CharField(max_length=200)
    direccion  = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
  
class Cuadro(models.Model):
    nombre           = models.CharField(max_length=100)
    galeria          = models.ForeignKey(Galeria, on_delete=models.CASCADE)
    autor            = models.CharField(max_length=100)
    fecha_creacion   = models.DateField(default=timezone.now)
    imagen           = models.ImageField(upload_to='img', blank=True)

class GaleriaForm(ModelForm):
    class Meta:
        model = Galeria
        fields = ['nombre', 'direccion']

class CuadroForm(ModelForm):
    class Meta:
        model = Cuadro
        fields = ['nombre', 'galeria', 'autor', 'fecha_creacion', 'imagen']