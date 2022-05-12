from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include
from . import views

urlpatterns = [
	path('mentores/', views.mentores_view, name="mentoresList"),
]
