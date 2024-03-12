from django.db import models

# Create your models here.


class Comprador(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    usuario = models.CharField(max_length=10)
    mail = models.EmailField()


    # Configuración para el manejo en el Panel de Administración

    class Meta:

        verbose_name = 'Comprador/a'
        verbose_name_plural = 'Compradores/as'
        ordering = ["apellido"]

    def __str__(self):

        return f"{self.apellido} {self.nombre}"
    

class Vendedor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    usuario = models.CharField(max_length=10)
    mail = models.EmailField()
    tel_contacto = models.IntegerField()

    class Meta:

        verbose_name = 'Vendedor/a'
        verbose_name_plural = 'Vendedores/as'
        ordering = ["apellido"]


    def __str__(self):

        return f"{self.apellido} {self.nombre}"
    


class Producto(models.Model):

    nombre_producto = models.CharField(max_length=60)
    precio = models.FloatField()

    class Meta:

        ordering = ["nombre_producto"]

    def __str__(self):

        return f"{self.nombre_producto}"
