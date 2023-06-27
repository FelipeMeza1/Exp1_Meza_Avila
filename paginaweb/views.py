from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Productos

# Create your views here.

def index(request):
    return render(request, 'paginaweb/index.html')

def mision(request):
    return render(request, 'paginaweb/mision.html')

def localizacion(request):
    return render(request, 'paginaweb/localizacion.html')

def formulario(request):
    return render(request, 'paginaweb/formulario.html')

def galeria(request):
    producto= Productos.objects.all()
    context={"producto":producto}
    return render(request, 'paginaweb/galeria.html', context)

def exit(request):
    logout(request)
    return redirect('index')