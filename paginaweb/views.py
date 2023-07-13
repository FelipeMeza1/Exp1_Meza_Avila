from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
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

@login_required
def exit(request):
    logout(request)
    return redirect('index')

def agregar(request):
    return render(request, 'paginaweb/agregar.html')

def agregarrec(request):
    a=request.POST['id']
    x=request.POST['foto']
    y=request.POST['nombre']
    z=request.POST['precio']
    b=request.POST['descripcion']
    prod=Productos(id=a, foto=x, nombre=y, precio=z, descripcion=b)
    prod.save()
    return redirect("/")

def actualizar(request, id):
    prod=Productos.objects.get(id=id)
    return render(request, 'paginaweb/actualizar.html',{'prod':prod})

def actualizarrec(request, id):
    a=request.POST['id']
    x=request.POST['foto']
    y=request.POST['nombre']
    z=request.POST['precio']
    b=request.POST['descripcion']
    prod=Productos.objects.get(id=id)
    prod.id=a
    prod.foto=x
    prod.nombre=y
    prod.precio=z
    prod.descripcion=b
    prod.save()
    return redirect("/")

def eliminar(request, id):
    prod=Productos.objects.get(id=id)
    prod.delete()
    return redirect("/")