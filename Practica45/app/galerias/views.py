# galerias/views.py

from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from .models import Galeria, GaleriaForm, Cuadro, CuadroForm
# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test_template(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'index.html', context)

def crear_galeria(request):
    form = GaleriaForm()
    state = 0
    errors = []
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
        'form': form, 
        'errors': errors, 
        'messages': messages,
        'state': state
        })

def consulta_galerias(request):
    galerias = Galeria.objects.all()
    return render(request, 'lista_galeria.html', {'galerias': galerias})

def modificar_galeria(request, pk):
    galeria = Galeria.objects.get(pk=pk)
    form = GaleriaForm(instance=galeria)
    state = 0
    errors = []
    messages = []
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
        'form': form, 
        'errors': errors, 
        'messages': messages,
        'state': state,
        'pk' : pk
        })

def eliminar_galeria(request, pk):
    galeria = Galeria.objects.get(pk=pk)
    nombre_galeria = galeria.nombre
    borrado = galeria.delete()
    errors = []
    messages = []
    if borrado[0] > 0:
        messages.append("Se ha eliminado la siguiente galeria: " + nombre_galeria)
    else:
        errors.append("Ha ocurrido algún error en el borrado")
    return render(request, 'eliminar_galeria.html', {
        'errors': errors,
        'messages': messages,
    })

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
        'form': form, 
        'errors': errors, 
        'messages': messages,
        'state': state
        })

def consulta_cuadros(request):
    cuadros = Cuadro.objects.all()
    return render(request, 'lista_cuadros.html', {'cuadros': cuadros})

def modificar_cuadro(request, pk):
    cuadro = Cuadro.objects.get(pk=pk) # TODO Implementar la posibilidad de que esto reviente
    form = CuadroForm(instance=cuadro)
    state = 0
    errors = []
    messages = []
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
        'form': form, 
        'errors': errors, 
        'messages': messages,
        'state': state,
        'pk' : pk
        })

def eliminar_cuadro(request, pk):
    cuadro = Cuadro.objects.get(pk=pk)
    nombre_cuadro = cuadro.nombre
    borrado = cuadro.delete()
    errors = []
    messages = []
    if borrado[0] > 0:
        messages.append("Se ha eliminado el siguiente cuadro: " + nombre_cuadro)
    else:
        errors.append("Ha ocurrido algún error en el borrado")
    return render(request, 'eliminar_cuadro.html', {
        'errors': errors,
        'messages': messages,
    })