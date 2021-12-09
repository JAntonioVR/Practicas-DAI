# galerias/views.py

from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from .models import Galeria, GaleriaForm, Cuadro
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
    return render(request, 'galeria_form.html', { 
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
