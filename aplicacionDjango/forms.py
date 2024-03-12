from django import forms

class ProductoForm(forms.Form):

    nombre_producto = forms.CharField(max_length=60, required=True)
    precio = forms.FloatField(required=True)


class VendedorForm(forms.Form):

    nombre = forms.CharField(max_length=40, required=True)
    apellido = forms.CharField(max_length=40, required=True)
    usuario = forms.CharField(max_length=10, required=True)
    mail = forms.EmailField(required=True)
    tel_contacto = forms.IntegerField(required=True)

class CompradorForm(forms.Form):

    nombre = forms.CharField(max_length=40, required=True)
    apellido = forms.CharField(max_length=40, required=True)
    usuario = forms.CharField(max_length=10, required=True)
    mail = forms.EmailField(required=True)