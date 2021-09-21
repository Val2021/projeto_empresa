from projeto_luizalabs.core.web.business.produto_business import do_read_produto_all
from projeto_luizalabs.core.web.business.empresa_business import do_delete_empresa, do_insert_empresa, do_read_empresa_all, do_read_empresa_by_id, do_update_empresa
from django.shortcuts import redirect, render



def empresa_control(request):
    empresas=list(do_read_empresa_all())
    for empresa in empresas:
        empresa["id"] = str(empresa["_id"])
    return render(request, "empresa_control.html", {"empresas":empresas,})


def empresa_insert(request):
    message = ""
    if request.method == "POST":
        cnpj = request.POST.get("cnpj")
        name = request.POST.get("name")
        corporate_name = request.POST.get("corporate_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        insert_doc = {
                      "cnpj": cnpj,
                      "name": name,
                      "corporate_name":corporate_name,
                      "email":email,
                      "phone": phone,
                      "produtos":[]}
        do_insert_empresa(insert_doc)
        message = "Inserido com sucesso!"
    return render(request, "empresa_insert.html", {"insert":True, "message":message,})


# def empresa_edit(request, empresaID):
#     message = ""
#     if request.method == "POST":
#         cnpj = request.POST.get("cnpj")
#         name = request.POST.get("name")
#         corporate_name = request.POST.get("corporate_name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         update_doc = {
#                       "cnpj": cnpj,
#                       "name": name,
#                       "corporate_name":corporate_name,
#                       "email":email,
#                       "phone": phone}
#         do_update_empresa(empresaID,update_doc)
#         message = "Editado com sucesso!"
#     empresa = do_read_empresa_by_id(empresaID)
#     empresa["_id"] = str(empresa["_id"])
#     empresa["id"] = empresa["_id"]
#     return render(request, "empresa_insert.html", { "message":message,"empresa":empresa})

def delete_empresa(request,empresaID,view=None):
    do_delete_empresa(empresaID)
    response = redirect("empresa:empresa_control")
    return response


def add_produto_empresa(request,empresaID):
    empresa = do_read_empresa_by_id(empresaID)
    if request.method == "POST":
        id_produto = request.POST.get("id_produto")
        produto_codigo = request.POST.get("produto_codigo")
        produto_preco = request.POST.get("produto_preco") 
        qtd_minima = request.POST.get("qtdmin")
        desconto = request.POST.get("descmax")
        produto_doc= {
            "id_produto":id_produto,
            "produto_codigo":produto_codigo,
            "produto_preco":produto_preco,
            "qtdmin":qtd_minima,
            "descmax":  desconto
        }
        empresa["produtos"].append(produto_doc)
        do_update_empresa(empresaID,empresa)
    produtos=list(do_read_produto_all())
    for produto in produtos:
        produto["id"] = str(produto["_id"])
    return render(request, "add_produto_empresa.html", {"produtos":produtos,"empresa":empresa})


