from .logic import reservas_logic as vl
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from monitoring.auth0backend import getRole
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required




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



@login_required
def variable_list(request):
    role = getRole(request)
    if role == "Gerencia Campus":
        variables = get_variables()
        context = {
            'variable_list': variables
        }
        return render(request, 'Variable/variables.html', context)
    else:
        return HttpResponse("Unauthorized User")













