from django.db import models


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=25, unique=True)
    correo = models.CharField(max_length=50, unique=True)
    clave = models.CharField(max_length=50)
    permiso = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre + ', ' + self.clave + ', ' + self.correo
