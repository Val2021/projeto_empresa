from projeto_luizalabs.empresa.views import *
from .views import *
from django.urls import path

app_name = "empresa"

urlpatterns = [
  
    path('controle_empresa',empresa_control, name="empresa_control"),
    ]