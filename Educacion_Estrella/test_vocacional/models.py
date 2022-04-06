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
import random
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL


class Pregunta(models.Model):
    NUM_DE_RESPUESTAS_PERMITIDAS = 1

    texto = models.TextField(verbose_name='Texto de la pregunta', default=None)
    max_puntaje = models.DecimalField(verbose_name='Máximo puntaje', default=3, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.texto

class TestUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puntaje_total = models.DecimalField(
        verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10)

    def crear_intentos(self,pregunta):
        intento = PreguntasRespondidas(pregunta=pregunta,testUsuario=self)
        intento.save()

    def obtener_nuevas_preguntas(self):
        respondidas = PreguntasRespondidas.objects.filter(testUsuario=self).values_list('pregunta__pk',flat=True)
        preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        if not preguntas_restantes.exists():
            return None
        return random.choice(preguntas_restantes)

    def validar_intento(self, pregunta_respondida, respuesta_seleccionada):
        if pregunta_respondida.pregunta_id != respuesta_seleccionada.pregunta_id:
            return
        
        pregunta_respondida.respuesta_seleccionada = respuesta_seleccionada
        if respuesta_seleccionada.correcta is True:
            pregunta_respondida.correcta = True
            pregunta_respondida.puntaje_obtenido = respuesta_seleccionada.pregunta.max_puntaje
            pregunta_respondida.respuesta = respuesta_seleccionada
        else:
            pregunta_respondida.respuesta = respuesta_seleccionada
        pregunta_respondida.save()
        self.actualizar_puntaje()

    def actualizar_puntaje(self):
        puntaje_actualizado = self.intentos.filter(correcta=True).aggregate(models.Sum('puntaje_obtenido')['puntaje_obtenido__sum'])
        self.puntaje_total = puntaje_actualizado
        self.save()
class ElegirRespuesta(models.Model):
    MAXIMO_RESPUESTA = 4

    pregunta = models.ForeignKey(
        Pregunta, related_name='opciones', on_delete=models.CASCADE)
    correcta = models.BooleanField(
        verbose_name='¿Es esta la pregunta correcta?', default=False, null=False)
    texto = models.TextField(verbose_name='Texto de la respuesta')

    def __str__(self):
        return self.texto


class PreguntasRespondidas(models.Model):
    testUsuario = models.ForeignKey(TestUsuario, on_delete=models.CASCADE, related_name='intentos')
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(
        ElegirRespuesta, on_delete=models.CASCADE, related_name='intentos', null=True)
    correcta = models.BooleanField(
        verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
    puntaje_obtenido = models.DecimalField(
        verbose_name='Puntaje obtenido', default=0, decimal_places=2, max_digits=6)
