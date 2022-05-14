from .logic import reservas_logic as vl
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



@login_required
@csrf_exempt
def reservas_view(request):
    reservas = vl.get_muchas()
    context = {
        'reserva_list': reservas
    }
    return render(request, 'reservas.html', context)

   

@login_required
def obtener_reserva(request, id=0):
    reserva = vl.get_reservas(id)
    context = {
        'reserva': reserva
    }
    return render(request, 'unico.html', context)















