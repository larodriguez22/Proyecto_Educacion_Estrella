

from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include



urlpatterns = [
   
    path('reservas/', views.reservas_view, name='variableList'), 
   ## path('', views.reservas_view, name='reservas_view'),
    path('<int:pk>', views.reserva_view, name='reserva_view'),
]
