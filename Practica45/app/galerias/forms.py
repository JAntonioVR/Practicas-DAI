#
# ────────────────────────────────────────────────────────────────────────────────────
#   :::::: galerias/forms.py : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────────────────────
#

# ─── IMPORTS ────────────────────────────────────────────────────────────────────
from django.forms import ModelForm, CharField, PasswordInput
from .models import Galeria, Cuadro
from django.contrib.auth.models import User
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

# ─── UserForm ───────────────────────────────────────────────────────────────────
class UserForm(ModelForm):
    class Meta:
        model = User
        password = CharField(widget=PasswordInput)
        fields = ['username', 'password', 'email']
        widgets = {
            'password': PasswordInput
        }

# ────────────────────────────────────────────────────────────────────────────────
