from django.db import models

from mentor.models import Mentor
from estudiante.models import Estudiante



class Reserva(models.Model):
    PSICOLOGIA = 'PL'
    MENTORIA = 'MT'
    ACADEMICA = 'AM'
    TYPE_CHOICES = [
        (PSICOLOGIA, 'Psicologia'),
        (MENTORIA, 'Mentoria'),
        (ACADEMICA, 'Academica'),
            
    ]
    fecha = models.DateTimeField(['%y-%m-%d'], blank=True, null=True)
    tipo = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default='',
    )
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, default=None)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '{}'.format(self.fecha)

    def __str__(self):
        return '{}'.format(self.tipo)
   




    
