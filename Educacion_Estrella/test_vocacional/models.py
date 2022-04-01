from email.policy import default
from django.db import models
from pregunta.models import Pregunta

# Create your models here.

class Test_Vocacional(models.Model):
    idTest = models.IntegerField(null = True, default = None)
    finalResult = None
    testDate = models.DateTimeField(auto_now_add=True)
    questions = models.ForeignKey(Pregunta, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '%s %s %s' % (self.idTest, self.finalResult, self.testDate)
        return '{}'.format(self.name)
        