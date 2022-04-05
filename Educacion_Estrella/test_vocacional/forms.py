from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Pregunta, PreguntasRespondidas, Usuario, ElegirRespuesta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model


class ElegirInlineFormset(forms.BaseInlineFormSet):
    def clean(self) -> None:
        super(ElegirInlineFormset, self).clean()

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


class RegistroFormulario(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    """ class Meta: """
    model = User

    fields = [
        'first_name',
        'last_name',
        'username',
        'email',
        'password1',
        'password2'
    ]