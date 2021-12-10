#
# ────────────────────────────────────────────────────────────────────────────────────
#   :::::: galerias/forms.py : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────────────────────
#

# ─── IMPORTS ────────────────────────────────────────────────────────────────────
from django.forms import ModelForm
from .models import Galeria, Cuadro

#
# ────────────────────────────────────────────────────────────────────────
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
