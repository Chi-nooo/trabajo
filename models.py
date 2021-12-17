from django.db import models

# Create your models here.
class Persona(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=100)
    nacimiento = models.CharField(max_length=50,blank=True)
    edad = models.CharField(max_length=50)
    foto = models.ImageField(
        upload_to = 'foto/%Y/%m/%d',
        blank = True,
        verbose_name = ('Foto del cliente')
    )

class Meta:
    verbose_name = ('cliente')
    verbose_name_plural = ('clientes')

def __str__(self):
    return self.nombre