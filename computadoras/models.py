from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Computadora(models.Model):
    modelo = models.CharField(max_length=100)
    procesador = models.CharField(max_length=100)
    ram = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)

    def __str__(self):
        return self.modelo
