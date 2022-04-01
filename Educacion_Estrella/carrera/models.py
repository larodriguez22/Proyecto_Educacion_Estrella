from enum import Flag
from unicodedata import name
from django.db import models

# Create your models here.


class Carrera(models.Model):
    name = models.CharField(null=False, max_length=50)
    area = models.CharField(null=False, max_length=50)
    university = models.CharField(null=False, max_length=50)

    def __str__(self):
        return '%s %s' % (self.area, self.university)
        return '{}'.format(self.name)
