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
    return render(request, 'galeria_form.html', { 
        'form': form, 
        'errors': errors, 
        'messages': messages,
        'state': state
        })

def consulta_galerias(request):
    galerias = Galeria.objects.all()
    return render(request, 'lista_galeria.html', {'galerias': galerias})
