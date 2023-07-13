from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Productos, Carrito, ItemCarrito
from django.http import JsonResponse
import json
from django.contrib import messages
import uuid

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

def carrito(request):
    return render(request, 'paginaweb/carrito.html')

def agregar_carrito(request):
    data = json.loads(request.body)
    product_id = data["id"]
    producto = Productos.objects.get(id=product_id)
    
    
    if request.user.is_authenticated:
        carrito, created = Carrito.objects.get_or_create(user=request.user, completed=False)
        itemscarrito, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
        itemscarrito.cantidad += 1
        itemscarrito.save()
        numero_de_items = carrito.numero_de_items
        
    else:
        
        try:
            cart = Cart.objects.get(session_id = request.session['nonuser'], completed=False)
            itemscarrito, created =ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
            itemscarrito.cantidad += 1
            itemscarrito.save()
            numero_de_items = carrito.numero_de_items
            
        
        except:
            request.session['nonuser'] = str(uuid.uuid4())
            cart = Cart.objects.create(session_id = request.session['nonuser'], completed=False)
            itemscarrito, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
            itemscarrito.cantidad += 1
            itemscarrito.save()
            numero_de_items = cart.numero_de_items
        
    
        print(itemscarrito)
    return JsonResponse(numero_de_items, safe=False)

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