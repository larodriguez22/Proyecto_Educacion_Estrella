from .logic import reservas_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate



@csrf_exempt
def reserva_view(request, pk):
    if request.method == 'GET':
        user = authenticate(username='test', password='test1234')
        if user is not None:
            reserva_dto = vl.get_variables(pk)
            reserva = serializers.serialize('json', reserva_dto,)
            return HttpResponse(reserva, 'application/json')
        else:
            print("Ha ocurrido un error, por favor inicie sesion")
            return HttpResponse("Ha ocurrido un error, por favor inicie sesion")
   
@csrf_exempt
def reservas_view(request):
    user = authenticate(username='test', password='test1234')
    print(user)
    if user is not None:
        print("entro")
        reservas_dto = vl.get_muchas()
        reservas = serializers.serialize('json', reservas_dto,)
        return HttpResponse(reservas, 'application/json')

    else:
        # print("Ha ocurrido un error, por favor inicie sesion")
        # return HttpResponse("Ha ocurrido un error, por favor inicie sesion")
        reservas_dto = vl.get_muchas()
        reservas = serializers.serialize('json', reservas_dto,)
        return HttpResponse(reservas, 'application/json')

