




from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   
    path('<int:pk>', views.reserva_view, name='reserva_view'),
]
