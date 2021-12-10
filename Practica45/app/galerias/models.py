#
# ──────────────────────────────────────────────────────────────────────────────────────
#   :::::: galerias/models.py : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────────────────
#

# ─── IMPORTS ────────────────────────────────────────────────────────────────────
from django.db import models
from django.utils import timezone
from django.forms import ModelForm

#
# ────────────────────────────────────────────────────────────────
#   :::::: M O D E L O S : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────
#

# ─── GALERIA ────────────────────────────────────────────────────────────────────
class Galeria(models.Model):
    nombre     = models.CharField(max_length=200)
    direccion  = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# ─── CUADRO ─────────────────────────────────────────────────────────────────────
class Cuadro(models.Model):
    nombre           = models.CharField(max_length=100)
    galeria          = models.ForeignKey(Galeria, on_delete=models.CASCADE)
    autor            = models.CharField(max_length=100)
    fecha_creacion   = models.DateField(default=timezone.now, blank=True, null=True)
    imagen           = models.ImageField(upload_to='img/', blank=True)

#
# ────────────────────────────────────────────────────────────── I ──────────
#   :::::: F O R M U L A R I O S : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────────
#

# ─── GaleriaForm ────────────────────────────────────────────────────────────────
# Formulario para crear o modificar una galería
class GaleriaForm(ModelForm):
    class Meta:
        model = Galeria
        fields = ['nombre', 'direccion']

# ─── CuadroForm ─────────────────────────────────────────────────────────────────
# Formulario para crear o modificar un cuadro
class CuadroForm(ModelForm):
    class Meta:
        model = Cuadro
        fields = ['nombre', 'galeria', 'autor', 'fecha_creacion', 'imagen']

# ────────────────────────────────────────────────────────────────────────────────
