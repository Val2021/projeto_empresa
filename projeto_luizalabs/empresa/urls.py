from projeto_luizalabs.empresa.views import *
from .views import *
from django.urls import path

app_name = "empresa"

urlpatterns = [
  
    path('controle_empresa',empresa_control, name="empresa_control"),
    path('inserir_empresa',empresa_insert, name="empresa_insert"),
    # path('editar_empresa/<str:empresaID>',empresa_edit, name="empresa_edit"),
    # path('deletar_empresa/<str:empresaID>',delete_empresa, name="delete_empresa"),
    path('inserir_produto',produto_insert, name="produto_insert"),
    path('controle_produtos',produto_control, name="produto_control"),
    path('produto_empresa/<str:empresaID>',produto_empresa, name="produto_empresa"),
    # path('deletar_produto/<str:produtoID>',delete_produto, name="delete_produto"),
    path('Inserir_produto_empresa/<str:empresaID>',add_produto_empresa, name="add_produto_empresa"),
    #------------------------Rotas de API-------------------------------------------------------
    path('api/relacao_empresas',api_get_empresa_all, name = "api_get_empresa_all"),
    path('api/relacao_produtos',api_get_produto_all, name = "api_get_produto_all"),
    path('api/cadastrar_produtos', api_cadastrar_produto, name = " api_cadastrar_produto"),
    path('api/cadastrar_empresas',api_cadastrar_empresa, name = "api_cadastrar_empresa"),
    path('api/adicionar_produto_empresa',api_add_produtoEmpresa, name = "api_add_produtoEmpresa"),
    path('api/delete_produto_empresa',api_delete_produtoEmpresa, name = "api_delete_produtoEmpresa"),

    ]