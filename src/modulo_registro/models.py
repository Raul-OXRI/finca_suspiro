from django.db import models
from .choices import GENERO
from django.contrib.auth.models import User, Group

# Create your models here.

class Registro(models.Model):
    # ********* DATOS DEL REGISTRO DE VACAS *********
    no_animal = models.IntegerField(blank=False, verbose_name='No. Animal')
    codigo = models.IntegerField(blank=False, verbose_name='Codigo')
    propietario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Propietario', null=True, default=None)
    #usuario = models.ManyToManyField(User, verbose_name='Propietario')
    fecha_nacimiento = models.DateField(blank=False, verbose_name='Fecha de nacimiento')
    genero = models.CharField(max_length=16, choices=GENERO, verbose_name='Genero')
    edad = models.IntegerField(blank=False, verbose_name='Edad')
    partos = models.IntegerField(blank=False, verbose_name='Partos')
    desendencia = models.IntegerField(blank=False, verbose_name='Desendencia')
    observaciones = models.TextField(blank=True, verbose_name='Observaciones')
    
def check_toro(sender, instance, **kwargs):
    if instance.genero == 'toro':
        instance.partos = 0