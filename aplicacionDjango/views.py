from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.



def home(request):

    return render(request, 'aplicacionDjango/index.html')


def comprador(request):

    contexto = {
        "Compradores" : Comprador.objects.all()
    }

    return render(request, 'aplicacionDjango/comprador.html', contexto)

def vendedor(request):

    contexto = {
        "Vendedores" : Vendedor.objects.all()
    }

    return render(request, 'aplicacionDjango/vendedor.html', contexto)

def producto(request):

    contexto = {
        "Productos" : Producto.objects.all()
    }

    return render(request, 'aplicacionDjango/producto.html', contexto)

# FORMULARIOS

def comprador_form(request):

    if request.method == "POST":
        mi_form = CompradorForm(request.POST)

        if mi_form.is_valid():

            comprador_nombre = mi_form.cleaned_data.get("nombre")
            comprador_apellido = mi_form.cleaned_data.get("apellido")
            comprador_usuario = mi_form.cleaned_data.get("usuario")
            comprador_mail = mi_form.cleaned_data.get("mail")

            comprador = Comprador(nombre=comprador_nombre, apellido=comprador_apellido, usuario = comprador_usuario, mail=comprador_mail)
            comprador.save()

            contexto = {

                "Compradores" : Comprador.objects.all()
            }


            return render(request, 'aplicacionDjango/comprador.html', contexto)
            
    
    else:
        mi_form = CompradorForm()

    return render(request, 'aplicacionDjango/comprador_form.html', {'form' : mi_form})




def vendedor_form(request):

    if request.method == "POST":
        mi_form = VendedorForm(request.POST)

        if mi_form.is_valid():

            vendedor_nombre = mi_form.cleaned_data.get("nombre")
            vendedor_apellido = mi_form.cleaned_data.get("apellido")
            vendedor_usuario = mi_form.cleaned_data.get("usuario")
            vendedor_mail = mi_form.cleaned_data.get("mail")
            vendedor_tel = mi_form.cleaned_data.get("tel_contacto")

            vendedor = Vendedor(nombre=vendedor_nombre, apellido=vendedor_apellido, usuario=vendedor_usuario, mail=vendedor_mail, tel_contacto=vendedor_tel)
            vendedor.save()

            contexto = {
                
                "Vendedores" : Vendedor.objects.all()
            }

            return render(request, 'aplicacionDjango/vendedor.html', contexto)
        
    
    else:
        mi_form = VendedorForm()
    
    return render(request, 'aplicacionDjango/vendedor_form.html', {'form' : mi_form})


def producto_form(request):

    if request.method == "POST":
        mi_form = ProductoForm(request.POST)

        if mi_form.is_valid():

            producto_nombre = mi_form.cleaned_data.get("nombre_producto")
            producto_precio = mi_form.cleaned_data.get("precio")
    

            producto = Producto(nombre_producto=producto_nombre, precio=producto_precio)
            producto.save()

            contexto = {
                "Productos" : Producto.objects.all()
            }

            return render(request, 'aplicacionDjango/producto.html', contexto)
        
    
    else:
        mi_form = ProductoForm()
    
    return render(request, 'aplicacionDjango/producto_form.html', {'form' : mi_form})

        
# Formulario de busqueda

def busqueda_producto(request):

    return render(request, 'aplicacionDjango/buscar.html')

def encontrar_producto(request):

    if request.GET["buscar"]:

        patron = request.GET["buscar"]
        producto = Producto.objects.filter(nombre_producto__icontains=patron)
        contexto = {

            "Productos" : producto
        }

        return render(request, 'aplicacionDjango/producto.html', contexto)
    
    contexto = {

        "Productos" : Producto.objects.all()
    }

    return render(request, 'aplicacionDjango/producto.html', contexto)