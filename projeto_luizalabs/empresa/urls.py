from projeto_luizalabs.empresa.views import *
from .views import *
from django.urls import path

app_name = "empresa"

urlpatterns = [
  
    path('controle_empresa',empresa_control, name="empresa_control"),
    path('inserir_empresa',empresa_insert, name="empresa_insert"),
    path('editar_empresa/<str:empresaID>',empresa_edit, name="empresa_edit"),
    path('deletar_empresa/<str:empresaID>',delete_empresa, name="delete_empresa"),
    path('inserir_produto',produto_insert, name="produto_insert"),
    path('controle_produtos',produto_control, name="produto_control"),
    
    ]