from projeto_luizalabs.core.web.business.produto_business import do_insert_produto, do_read_produto_all, do_update_produto
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from projeto_luizalabs.core.web.business.empresa_business import do_insert_empresa, do_read_empresa_all, do_read_empresa_by_id, do_update_empresa


def api_get_empresa_all(request):
    if request.method == "GET":
        empresas = list(do_read_empresa_all())
        for empresa in empresas:
            empresa["_id"] = str(empresa["_id"])
        return JsonResponse({"empresas":empresas})

def api_get_produto_all(request):
    if request.method == "GET":
        produtos = list(do_read_produto_all())
        for produto in produtos:
            produto["_id"] = str(produto["_id"])
        return JsonResponse({"produtos":produtos})

#____Cadastrar produtos___________________________
@csrf_exempt
def api_cadastrar_produto(request):
     if request.method == "POST":
        data_json = json.loads(request.body)
        produtos = data_json["produtos"]
        list_ids=[]
        for produto in produtos:
            inserted_id = do_insert_produto(produto)
            list_ids.append({produto["produto_nome"]:inserted_id})
        return JsonResponse({"list_ids":list_ids})

#___Cadastrar empresa_______________________________________
@csrf_exempt
def api_cadastrar_empresa(request):
     if request.method == "POST":
        data_json = json.loads(request.body)
        empresa = data_json["empresa"]
        inserted_id = do_insert_empresa(empresa)
        return JsonResponse({"inserted_id":inserted_id})

#__cadastrar produto na empresa________________________
@csrf_exempt
def api_add_produtoEmpresa(request):
     if request.method == "POST":
        data_json = json.loads(request.body)
        id_empresa = data_json["id_empresa"]
        produto = data_json["produtos"]
        print("id_empresa",id_empresa,produto)
        empresa=do_read_empresa_by_id(id_empresa)
        empresa["produtos"] = produto
        print("chave",empresa["produtos"])
        inserted_id = do_update_empresa(id_empresa,empresa)
        return JsonResponse({"inserted_id":inserted_id})
