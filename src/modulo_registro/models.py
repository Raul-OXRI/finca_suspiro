from django.db import models
from .choices import GENERO
from django.contrib.auth.models import User, Group

# Create your models here.


class Registro(models.Model):
    # ********* DATOS DEL REGISTRO DE VACAS *********
    no_animal = models.IntegerField(blank=False)
    codigo = models.IntegerField(blank=False)
    fecha_nacimiento = models.DateField(blank=False, verbose_name='Fecha de nacimiento')
    genero = models.CharField(max_length=16, choices=GENERO)
    edad = models.IntegerField(blank=False)
    partos = models.IntegerField(blank=False)
    desendencia = models.IntegerField(blank=False)
    observaciones = models.TextField(blank=True)
    usuario = models.ManyToManyField(User, verbose_name='Usuarios')