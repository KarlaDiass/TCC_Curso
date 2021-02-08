from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('historico', views.historico_consultas, name='historico'),
    path('historico_familiar', views.historico_familiar, name='historico-familiar'),
]