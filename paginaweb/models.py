from django.db import models

# Create your models here.

class Productos(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    foto = models.ImageField()
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return self.id