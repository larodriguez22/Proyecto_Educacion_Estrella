from .logic import reservas_logic as vl
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate


from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

   

@csrf_exempt
def reserva_view(request, id=0):
    if request.method == 'GET':
        user = authenticate(username='test', password='test1234')
        if user is not None:
            reserva = vl.get_reservas(id)
            context = {
                'reserva': reserva
            }
            return render(request, 'unico.html', context)

           
        else:
            print("Ha ocurrido un error, por favor inicie sesion")
            return HttpResponse("Ha ocurrido un error, por favor inicie sesion")
   



@csrf_exempt
def reservas_view(request):
    user = authenticate(username='test', password='test1234')
    print(user)
    if user is not None:
        print("entro")
        reservas = vl.get_muchas()
        context = {
        'reserva_list': reservas
        }
        return render(request, 'reservas.html', context)
        
    else:
        # print("Ha ocurrido un error, por favor inicie sesion")
        # return HttpResponse("Ha ocurrido un error, por favor inicie sesion")
        reservas = vl.get_muchas()
        context = {
        'reserva_list': reservas
        }
        return render(request, 'reservas.html', context)

