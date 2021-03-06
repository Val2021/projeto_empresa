from projeto_luizalabs.core.web.business.produto_business import do_insert_produto, do_read_produto_all, do_update_produto
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from projeto_luizalabs.core.web.business.empresa_business import do_insert_empresa, do_read_empresa_all, do_read_empresa_by_id, do_update_empresa



#-----API-listar--empresas--cadastradas---
def api_get_empresa_all(request):
    if request.method == "GET":
        empresas = list(do_read_empresa_all())
        for empresa in empresas:
            empresa["_id"] = str(empresa["_id"])
        return JsonResponse({"empresas":empresas})


#-----API-listar--produtos--cadastrados---
def api_get_produto_all(request):
    if request.method == "GET":
        produtos = list(do_read_produto_all())
        for produto in produtos:
            produto["_id"] = str(produto["_id"])
        return JsonResponse({"produtos":produtos})



#-----API-cadastrar--produtos--------------------------------
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

#-----API-cadastrar--empresas--------------------------------
@csrf_exempt
def api_cadastrar_empresa(request):
     if request.method == "POST":
        data_json = json.loads(request.body)
        empresa = data_json["empresa"]
        inserted_id = do_insert_empresa(empresa)
        return JsonResponse({"inserted_id":inserted_id})


#-----API-cadastrar--produtos-em-uma-empresa--------------------------------
@csrf_exempt
def api_add_produtoEmpresa(request):
     if request.method == "POST":
        data_json = json.loads(request.body)
        id_empresa = data_json["id_empresa"]
        produto = data_json["produtos"]
        empresa=do_read_empresa_by_id(id_empresa)
        empresa["produtos"].extend(produto)
        inserted_id = do_update_empresa(id_empresa,empresa)
        return JsonResponse({"inserted_id":inserted_id})

#-----API-remover--produtos-de-uma-empresa--------------------------------
@csrf_exempt
def api_delete_produtoEmpresa(request):
     if request.method == "DELETE":
        data_json = json.loads(request.body)
        id_empresa = data_json["id_empresa"]
        produtos = data_json["produtos"]
        empresa=do_read_empresa_by_id(id_empresa)
        for id_produto in produtos:
            for produto in empresa["produtos"]:
                if id_produto == produto["id_produto"]:
                    empresa["produtos"].remove(produto)
        inserted_id = do_update_empresa(id_empresa,empresa)
        return JsonResponse({"inserted_id":inserted_id})


