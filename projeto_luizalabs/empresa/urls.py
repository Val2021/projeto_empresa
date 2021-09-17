from projeto_luizalabs.empresa.views import *
from .views import *
from django.urls import path

app_name = "empresa"

urlpatterns = [
  
    path('controle_empresa',empresa_control, name="empresa_control"),
    path('inserir_empresa',empresa_insert, name="empresa_insert"),
    path('editar_empresa/<str:empresaID>',empresa_edit, name="empresa_edit"),
    ]