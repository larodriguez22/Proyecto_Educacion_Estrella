from email.policy import default
from unittest import result
from django.db import models

# Create your models here.

class Test_Vocacional(models.Model):
    idTest = models.IntegerField(null = True, default = None)
    finalResult = None
    testDate = models.DateTimeField(auto_now_add=True)

