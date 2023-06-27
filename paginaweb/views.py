from django.shortcuts import render

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
    return render(request, 'paginaweb/galeria.html')
