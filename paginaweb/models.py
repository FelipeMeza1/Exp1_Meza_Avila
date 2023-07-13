from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Productos(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    foto = models.ImageField()
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return self.id

class Carrito(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    usuario = models.OneToOneField(User,  on_delete=models.CASCADE, blank=True, null=True)
    completo = models.BooleanField(default=False)
    session_id = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def precio_total(self):
        itemscarrito = self.itemscarrito.all()
        total = sum([item.precio for item in itemscarrito])
        return total
    
    
      
    @property
    def numero_de_items(self):
        itemscarrito = self.itemscarrito.all()
        cantidad = sum([item.cantidad for item in itemscarrito])
        return cantidad
    

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name='items')
    carrito = models.ForeignKey(Carrito, on_delete= models.CASCADE, related_name="itemscarrito")
    cantidad = models.IntegerField(default=0)
    
    def __str__(self):
        return self.producto.nombre
    
    @property
    def precio(self):
        precionuevo = self.producto.precio * self.quantity
        return precionuevo