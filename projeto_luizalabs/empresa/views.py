from projeto_luizalabs.core.web.business.produto_business import do_insert_produto, do_read_produto_all, do_read_produto_empresaName
from projeto_luizalabs.core.web.business.empresa_business import do_delete_empresa, do_insert_empresa, do_read_empresa_all, do_read_empresa_by_id, do_update_empresa
from django.shortcuts import redirect, render



def empresa_control(request):
    empresas=list(do_read_empresa_all())
    print("empresas",empresas)
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
                      "phone": phone}
        do_insert_empresa(insert_doc)
        message = "Inserido com sucesso!"
    return render(request, "empresa_insert.html", {"insert":True, "message":message,})


def empresa_edit(request, empresaID):
    message = ""
    if request.method == "POST":
        cnpj = request.POST.get("cnpj")
        name = request.POST.get("name")
        corporate_name = request.POST.get("corporate_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        update_doc = {
                      "cnpj": cnpj,
                      "name": name,
                      "corporate_name":corporate_name,
                      "email":email,
                      "phone": phone}
        do_update_empresa(empresaID,update_doc)
        message = "Editado com sucesso!"
    empresa = do_read_empresa_by_id(empresaID)
    empresa["_id"] = str(empresa["_id"])
    empresa["id"] = empresa["_id"]
    return render(request, "empresa_insert.html", { "message":message,"empresa":empresa})

def delete_empresa(request,empresaID,view=None):
    do_delete_empresa(empresaID)
    response = redirect("empresa:empresa_control")
    return response


def produto_insert(request):
    message = ""
    if request.method == "POST":
        produto_codigo = request.POST.get("produto_codigo")
        produto_nome = request.POST.get("produto_nome")
        produto_preco = request.POST.get("produto_preco")
        qtdmin = request.POST.get("qtdmin")
        descmax = request.POST.get("descmax")
        empresa = request.POST.get("empresa")
        insert_doc = {
                      "produto_codigo":produto_codigo,
                      "produto_nome": produto_nome,
                      "produto_preco":produto_preco,
                      "qtdmin":qtdmin,
                      "descmax":descmax,
                      "empresa":empresa,
                      }
        do_insert_produto(insert_doc)
        message = "Inserido com sucesso!"
    empresas = list(do_read_empresa_all())
    print("empresas",empresas)
    for empresa in empresas:
        empresa["_id"] = str(empresa["_id"])
        empresa["id"] = empresa["_id"]
    return render(request, "produto_insert.html", {"insert":True, "empresas": empresas,"message":message,})


def produto_control(request):
    produtos=list(do_read_produto_all())
    print("produto",produtos)
    for produto in produtos:
        produto["id"] = str(produto["_id"])
    return render(request, "produto_control.html", {"produtos":produtos,})

def produto_empresa(request,empresaID):
    empresa = do_read_empresa_by_id(empresaID)
    empresa_name = str(empresa["name"])
    produtos = do_read_produto_empresaName(empresa_name)
    produto_codigo = produtos["produto_codigo"] 
    produto_nome = produtos["produto_nome"]
    produto_preco = produtos["produto_preco"] 
    qtd_minima = produtos["qtdmin"] 
    desconto = produtos["descmax"] 
    empresa_nome = produtos["empresa"] 
    return render(request, "empresa_produto.html", {"produtos":produtos,"produto_codigo":produto_codigo,"produto_nome":produto_nome,"produto_preco":produto_preco,"qtd_minima":qtd_minima,"desconto":desconto,"empresa_nome":empresa_nome})


