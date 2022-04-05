




from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   
    path('', views.reservas_view, name='reservas_view'),
    path('<int:pk>', views.reserva_view, name='reserva_view'),
]
