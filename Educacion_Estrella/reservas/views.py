from .logic import reservas_logic as vl
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from Educacion_Estrella.auth0backend import getRole
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



@login_required
@csrf_exempt
def reservas_view(request):
    role = getRole(request)
    if role == "Mentor":
        reservas = vl.get_muchas()
        context = {
            'reservas_view': reservas
        }
        return render(request, 'Reserva/reservas.html', context)
    else:
        return HttpResponse("Unauthorized User")
















