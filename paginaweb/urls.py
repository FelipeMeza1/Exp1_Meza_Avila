from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    path('formulario/', views.formulario, name='formulario'),
    path('localizacion/', views.localizacion, name='localizacion'),
    path('mision/', views.mision, name='mision'),
    path('logout/', exit, name='exit'),
    path('agregar/', views.agregar, name='agregar'),
    path('agregarrec/', views.agregarrec, name='agregarrec'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('actualizar/<int:id>', views.actualizar, name='actualizar'),
    path('actualizar/actualizarrec/<int:id>/', views.actualizarrec, name='actualizarrec'),
    path("carrito/", views.carrito, name="carrito"),
    path("agregar_carrito/", views.agregar_carrito, name= "agregar_carrito"),
]