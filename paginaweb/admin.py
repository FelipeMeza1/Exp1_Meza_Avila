from django.contrib import admin
from .models import Productos, Carrito, ItemCarrito

# Register your models here.

admin.site.register([Productos, Carrito, ItemCarrito])