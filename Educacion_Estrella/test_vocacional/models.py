""" from email.policy import default
from django.db import models
from pregunta.models import Pregunta
from pregunta.models import ElegirRespuesta
from pregunta.models import PreguntasRespondidas
from pregunta.models import Usuario """


# Create your models here.


""" class Test_Vocacional(models.Model):
    #finalResult = None
    testDate = models.DateTimeField(auto_now_add=True)
    questions = models.ManyToManyField(Pregunta, default=None)

    def __str__(self):
        return '%s %s' % (self.finalResult, self.testDate)
        return '{}'.format(self.name)
 """

from email.policy import default
from pyexpat import model
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL


class Pregunta(models.Model):
    NUM_RESPUESTAS_PERMITIDAS = 1

    texto = models.TextField(verbose_name='Texto de la pregunta', default=None)

    def __str__(self):
        return self.texto


class Usuario(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    puntaje_total = models.DecimalField(verbose_name='Puntaje Total',default=0,decimal_places=2, max_digits=10)

class ElegirRespuesta(models.Model):
    MAXIMO_RESPUESTA = 4

    pregunta = models.ForeignKey(
        Pregunta, related_name='preguntas', on_delete=models.CASCADE)
    correcta = models.BooleanField(
        verbose_name='¿Es esta la pregunta correcta?', default=False, null=False)
    texto = models.TextField(verbose_name='Texto de la respuesta')

    def __str__(self):
        return self.texto


class PreguntasRespondidas(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(
        ElegirRespuesta, on_delete=models.CASCADE, related_name='intentos')
    correcta = models.BooleanField(
        verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
    puntaje_obtenido = models.DecimalField(
        verbose_name='Puntaje obtenido', default=0, decimal_places=2, max_digits=6)
