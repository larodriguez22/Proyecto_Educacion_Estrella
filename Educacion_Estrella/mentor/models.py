from django.db import models

class Mentor(models.Model):
    
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)
   
