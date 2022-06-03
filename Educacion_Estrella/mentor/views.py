import json
from multiprocessing import context
import re
from django.shortcuts import render

from .logic import mentor_logic as ml
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Mentor

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.


@csrf_exempt
def mentores_view(request):

    mentores = ml.get_todos()
    context = {
        'mentores_view': mentores
    }
    return render(request, 'mentores.html', context)


def MentoresList(request):
    queryset = Mentor.objects.all()
    context = list(queryset.values('nombre'))
    return JsonResponse(context, safe=False)


def MentorCreate(request):
    if request.method == 'POST':
        try:
            data = request.body.decode('utf-8')
            data_json = json.loads(data)
            mentor = Mentor()
            mentor.nombre = data_json['nombre']
            mentor.save()
            return HttpResponse("Succesfully created mentor")
        except:
            return HttpResponse("Unsuccesfully created mentor")
