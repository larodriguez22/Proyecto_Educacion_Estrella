from .logic import reservas_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def reserva_view(request, pk):
    if request.method == 'GET':
        reserva_dto = vl.get_variables(pk)
        reserva = serializers.serialize('json', reserva_dto,)
        return HttpResponse(reserva, 'application/json')
   
@csrf_exempt
def reservas_view(request):
   
    reservas_dto = vl.get_muchas()
    reservas = serializers.serialize('json', reservas_dto,)
    return HttpResponse(reservas, 'application/json')

