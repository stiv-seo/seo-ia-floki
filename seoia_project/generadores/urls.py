from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generador-metadata/', views.generador_metadata, name='generador_metadata'),
    #path('generador-metadata/', views.generador_metadata, name='generador_metadata'),
    path('generador-articulos/', views.generador_articulos, name='generador_articulos'),
    path('generador-datos/', views.generador_datos, name='generador_datos'),
    path('generar-ficha-producto/', views.generador_ficha_producto, name='generador_ficha_producto'),
    path('auditoria-tecnica/', views.auditoria_tecnica, name='auditoria_tecnica'),
    path('topic-research/', views.topic_research, name='topic_research'),
]
