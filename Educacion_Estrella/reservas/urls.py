

from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include
from . import views


urlpatterns = [
   
    path('reservas/', views.reservas_view, name='reservaList'), 
   ## path('', views.reservas_view, name='reservas_view'),
    path('<int:pk>', views.reservas_view, name='reserva_view'),
]
