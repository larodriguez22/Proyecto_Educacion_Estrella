from cgitb import text
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
    text = models.CharField(max_length=250)
    answers = models.ForeignKey(
        Respuesta, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '%s' % (self.text)
        return '{}'.format(self.name)
