from unicodedata import name
from django.urls import path
from .views import inicio, registro, loginView, logoutView, HomeUsuario, jugar

urlpatterns = [
    path('', inicio, name='inicio'),
    path('HomeUsuario/', HomeUsuario, name='HomeUsuario'),
    path('login/', loginView, name='login'),
    path('registro/', registro, name='registro'),
    path('logout/', logoutView, name='logout'),
    path('jugar/', jugar, name='jugar'),
    
]
