from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include, url
from . import views

urlpatterns = [
	#path('mentores/', views.mentores_view, name="mentoresList"),
	url(r'^mentores/', views.MentoresList, name="mentoresList"),
    url(r'^mentorcreate/$', csrf_exempt(views.MentorCreate), name='mentorCreate'),
]
