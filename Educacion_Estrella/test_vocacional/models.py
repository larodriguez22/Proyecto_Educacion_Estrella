from email.policy import default
from django.db import models
from pregunta.models import Pregunta

# Create your models here.


class Test_Vocacional(models.Model):
    #finalResult = None
    testDate = models.DateTimeField(auto_now_add=True)
    questions = models.ManyToManyField(Pregunta, default=None)

    def __str__(self):
        return '%s %s' % (self.finalResult, self.testDate)
        return '{}'.format(self.name)
