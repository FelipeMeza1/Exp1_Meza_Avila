from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    path('formulario/', views.formulario, name='formulario'),
    path('localizacion', views.localizacion, name='localizacion'),
    path('mision', views.mision, name='mision'),
]