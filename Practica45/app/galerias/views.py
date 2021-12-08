# galerias/views.py

from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from .models import GaleriaForm, Cuadro
# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test_template(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'galerias/index.html', context)

def crear_galeria(request):

    form = GaleriaForm()
    if request.method == 'POST':
        '''
        form = GaleriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        '''
    return render(request, 'galerias/galeria_form.html', {'form': form})