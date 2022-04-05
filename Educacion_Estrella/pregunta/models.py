""" from cgitb import text
from enum import Flag
from typing import TextIO
from django.db import models

# Create your models here.


class Respuesta(models.Model):
    #id = models.IntegerField(null=False)
    text = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.text)
        return '{}'.format(self.name)


class Pregunta(models.Model):

    PREGUNTA1 = 'P1'
    PREGUNTA2 = 'P2'
    PREGUNTA3 = 'P3'
    PREGUNTA4 = 'P4'
    PREGUNTA5 = 'P5'
    TYPE_CHOICES = [
        (PREGUNTA1, '¿pregunnta 1?'),
        (PREGUNTA2, '¿pregunnta 2?'),
        (PREGUNTA3, '¿pregunnta 3?'),
        (PREGUNTA4, '¿pregunnta 4?'),
        (PREGUNTA5, '¿pregunnta 5?'),
            
    ]
    tipo = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default='',
    )

    answers = models.ForeignKey(
    Respuesta, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '%s' % (self.text)
        return '{}'.format(self.name)
 """

from django.db import  models

class Pregunta(models.Model):
    texto = models.TextField(verbose_name='Texto de la pregunta')

    def __str__(self):
        return self.texto

class Elegir_Respuesta(models.Model):
    MAXIMO_RESPUESTA = 4

    pregunta = models.ForeignKey(Pregunta, related_name='preguntas', on_delete=models.CASCADE)
    correcta = models.BooleanField(verbose_name='¿Es esta la pregunta correcta?',default=False,null=False)
    texto = models.TextField(verbose_name='Texto de la respuesta')

    def __str__(self):
        return self.texto
    
