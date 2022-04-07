""" from pyexpat import model
from django.contrib import admin
from .models import Pregunta

from .models import Respuesta
# Register your models here.

admin.site.register(Pregunta)

admin.site.register(Respuesta)
# Preguntar sobre añadir Respuesta



from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas


class ElegirRespuestaInLine(admin.TabularInline):
    model = ElegirRespuesta
    can_delete = False
    max_num = ElegirRespuesta.MAXIMO_RESPUESTA
    min_num = ElegirRespuesta.MAXIMO_RESPUESTA
class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines = (ElegirRespuestaInLine, )
    list_display = ['texto',]
    search_fields = ['texto', 'preguntas__texto']

class PreguntasRespondidasAdmin(admin.ModelAdmin):
    list_display = ['pregunta','respuesta', 'correcta', 'puntaje_obtenido']

    class Meta:
        model = PreguntasRespondidas


admin.site.register(PreguntasRespondidas)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ElegirRespuesta) """