from django.contrib import admin
""" from .models import Pregunta

from .models import Respuesta """
# Register your models here.

""" admin.site.register(Pregunta)

admin.site.register(Respuesta) """
# Preguntar sobre añadir Respuesta



from .models import Pregunta, Elegir_Respuesta

admin.site.register(Pregunta)
admin.site.register(Elegir_Respuesta)