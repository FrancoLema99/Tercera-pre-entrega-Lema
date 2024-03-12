from django.urls import path
from.views import *

urlpatterns = [
    path('', home, name='home'),
    path('comprador/', comprador, name='comprador'),
    path('vendedor/', vendedor, name='vendedor'),
    path('producto/', producto, name='producto'),

    # Fromularios

    path('vendedor_form/', vendedor_form, name='vendedor_form'),
    path('comprador_form/', comprador_form, name='comprador_form'),
    path('producto_form/', producto_form, name='producto_form'),

    # Formulario busqueda

    path('buscar_producto/', busqueda_producto, name='buscar_productos'),
    path('encontrar_producto/', encontrar_producto, name='encontrar_producto')
]