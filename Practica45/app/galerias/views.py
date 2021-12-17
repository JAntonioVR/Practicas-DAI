#
# ────────────────────────────────────────────────────────────────────────────────────
#   :::::: galerias/views.py : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────────────────────
#

# ─── IMPORTS ────────────────────────────────────────────────────────────────────
from django.shortcuts import render
from .models import Galeria, Cuadro
from .forms import GaleriaForm, CuadroForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import permission_required


# ─── HOME ───────────────────────────────────────────────────────────────────────
def index(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'index.html', context)

#
# ──────────────────────────────────────────────────────────────────
#   :::::: G A L E R I A S : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────
#

# ─── CREAR GALERIA ──────────────────────────────────────────────────────────────
@permission_required('galerias.add_galeria')
def crear_galeria(request):
    form     = GaleriaForm()
    state    = 0
    errors   = []
    messages = []
    if request.method == 'POST':
        form = GaleriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.append("La galeria se ha guardado con éxito.")
            state = 1
        else:
            errors.append("Los datos introducidos no eran válidos.")
            state = -1
    else:
        messages.append("Introduce los datos de la nueva galería:")
    return render(request, 'crear_galeria.html', { 
        'form'    : form,
        'errors'  : errors,
        'messages': messages,
        'state'   : state
        })

# ─── CONSULTA/LISTADO DE GALERIAS ───────────────────────────────────────────────
def consulta_galerias(request):
    galerias = Galeria.objects.all()
    return render(request, 'lista_galeria.html', {'galerias': galerias})

# ─── MODIFICAR GALERIA ──────────────────────────────────────────────────────────
@permission_required('galerias.change_galeria')
def modificar_galeria(request, pk):
    errors   = []
    messages = []
    state    = 0
    try:
        galeria = Galeria.objects.get(pk=pk)
    except ObjectDoesNotExist:
        state = -1
        return handle_exception(request, pk, 'modificar_galeria.html', 
        {'errors': errors, 'messages': messages, 'state': state, 'pk': pk})
    form = GaleriaForm(instance=galeria)
    if request.method == 'POST':
        form = GaleriaForm(request.POST, instance=galeria)
        if form.is_valid():
            form.save()
            messages.append("La galeria se ha modificado con éxito.")
            state = 1
        else:
            errors.append("Los datos introducidos no eran válidos.")
            state = -1
    return render(request, 'modificar_galeria.html', { 
        'form'    : form,
        'errors'  : errors,
        'messages': messages,
        'state'   : state,
        'pk'      : pk
        })

# ─── ELIMINAR GALERIA ───────────────────────────────────────────────────────────
@permission_required('galerias.delete_galeria')
def eliminar_galeria(request, pk):
    errors   = []
    messages = []
    try:
        galeria = Galeria.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return handle_exception(request, pk, 'eliminar_galeria.html', {'errors': errors, 'messages': messages})
    
    nombre_galeria = galeria.nombre
    borrado = galeria.delete()
    if borrado[0] > 0:
        messages.append("Se ha eliminado la siguiente galeria: " + nombre_galeria)
    else:
        errors.append("Ha ocurrido algún error en el borrado")
    return render(request, 'eliminar_galeria.html', {
        'errors'  : errors,
        'messages': messages,
    })

#
# ────────────────────────────────────────────────────────────────
#   :::::: C U A D R O S : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────
#

# ─── CREAR CUADRO ───────────────────────────────────────────────────────────────
@permission_required('galerias.add_cuadro')
def crear_cuadro(request):
    form = CuadroForm()
    state = 0
    errors = []
    messages = []
    if request.method == 'POST':
        form = CuadroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.append("El cuadro se ha guardado con éxito.")
            state = 1
        else:
            errors.append("Los datos introducidos no eran válidos.")
            state = -1
    else:
        messages.append("Introduce los datos del nuevo cuadro:")
    return render(request, 'crear_cuadro.html', { 
        'form'    : form,
        'errors'  : errors,
        'messages': messages,
        'state'   : state
        })

# ─── CONSULTA/LISTADO DE CUADROS ────────────────────────────────────────────────
def consulta_cuadros(request):
    cuadros = Cuadro.objects.all()
    return render(request, 'lista_cuadros.html', {'cuadros': cuadros})

# ─── MODIFICAR CUADRO ───────────────────────────────────────────────────────────
@permission_required('galerias.change_cuadro')
def modificar_cuadro(request, pk):
    state    = 0
    errors   = []
    messages = []
    try:
        cuadro = Cuadro.objects.get(pk=pk)
    except ObjectDoesNotExist:
        state = -1
        return handle_exception(request, pk, 'modificar_cuadro.html',
            {'errors': errors, 'messages': messages, 'state': state, 'pk':pk})
    form = CuadroForm(instance=cuadro)
    if request.method == 'POST':
        form = CuadroForm(request.POST, request.FILES, instance=cuadro)
        if form.is_valid():
            form.save()
            messages.append("El cuadro se ha modificado con éxito.")
            state = 1
        else:
            errors.append("Los datos introducidos no eran válidos.")
            state = -1
    return render(request, 'modificar_cuadro.html', { 
        'form'    : form,
        'errors'  : errors,
        'messages': messages,
        'state'   : state,
        'pk'      : pk
        })

# ─── ELIMINAR CUADRO ────────────────────────────────────────────────────────────
@permission_required('galerias.delete_cuadro')
def eliminar_cuadro(request, pk):
    errors   = []
    messages = []
    try:
        cuadro = Cuadro.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return handle_exception(request, pk, 'eliminar_cuadro.html', {'errors': errors, 'messages': messages} )
    nombre_cuadro = cuadro.nombre
    borrado = cuadro.delete()
    if borrado[0] > 0:
        messages.append("Se ha eliminado el siguiente cuadro: " + nombre_cuadro)
    else:
        errors.append("Ha ocurrido algún error en el borrado")
    return render(request, 'eliminar_cuadro.html', {
        'errors'  : errors,
        'messages': messages,
    })

# ────────────────────────────────────────────────────────────────────────────────

def handle_exception(request, id, template, args):
    error = "ERROR: No se ha encontrado el objeto de id " + str(id)
    if(not args['errors']):
        args['errors'] = []
    args['errors'].append(error)
    return render(request, template, args)
