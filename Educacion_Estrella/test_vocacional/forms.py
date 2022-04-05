from django import forms
from .models import Pregunta, PreguntasRespondidas, Usuario, ElegirRespuesta

class ElegirInlineFormset(forms.BaseInlineFormSet):
    def clean(self) -> None:
        super(ElegirInlineFormset,self).clean()
        
        respuesta_correcta = 0
        for formulario in self.forms:
            if not formulario.is_valid():
                return

            if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
                respuesta_correcta += 1
        try:
            assert respuesta_correcta == Pregunta.NUM_RESPUESTAS_PERMITIDAS
        except AssertionError:
            raise forms.ValidationError('Solamente se permite una respuesta')

