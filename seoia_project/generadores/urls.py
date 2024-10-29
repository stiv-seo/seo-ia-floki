from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generador-metadata/', views.generador_metadata, name='generador_metadata'),
    #path('generador-metadata/', views.generador_metadata, name='generador_metadata'),
    path('generador-articulos/', views.generador_articulos, name='generador_articulos'),
    path('generador-datos/', views.generador_datos, name='generador_datos'),
]
