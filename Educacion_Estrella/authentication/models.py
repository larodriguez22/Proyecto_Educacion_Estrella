from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    # MENTOR = 1
    # ESTUDIANTE = 2
    # ROLE_CHOICES = (
    #       (MENTOR, 'Doctor'),
    #       (ESTUDIANTE, 'Nurse'),
    #   )
    email = models.EmailField(
        max_length=150, unique=True)
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    
    # Los usuarios podrán iniciar sesión con el correo en lugar de usar su username
    USERNAME_FIELD = 'email'
    # Según la documentación, para obligar al usuario a introducir un campo debemos indicarlo en una lista
    # username y password se heredan de la clase AbstractUser
    REQUIRED_FIELDS = ['username', 'password']
