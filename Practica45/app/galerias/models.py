#
# ──────────────────────────────────────────────────────────────────────────────────────
#   :::::: galerias/models.py : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────────────────
#

# ─── IMPORTS ────────────────────────────────────────────────────────────────────
from django.db import models
from django.utils import timezone


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

# ────────────────────────────────────────────────────────────────────────────────
