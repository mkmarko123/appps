from django.db import models
from usuario.models import Usuario


# Create your models here.
class Finca(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='propietario')

    def __str__(self):
        return self.nombre


class Parcela(models.Model):
    finca_origen = models.ForeignKey(Finca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    latitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Tree(models.Model):  # * Solo pueden haber 10 arboles por parcela por año
    parcela_origen = models.ForeignKey(Finca, on_delete=models.CASCADE)
    diametro = models.CharField(max_length=50)
    altura = models.CharField(max_length=50)
    salud = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
