from django.shortcuts import render
from .logic import mentor_logic as ml
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

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
    return render(request, 'Mentor/mentores.html', context)

