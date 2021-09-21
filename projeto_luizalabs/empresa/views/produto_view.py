from projeto_luizalabs.core.web.business.empresa_business import do_read_empresa_all, do_read_empresa_by_id
from projeto_luizalabs.core.web.business.produto_business import do_delete_produto, do_insert_produto, do_read_produto_all, do_read_produto_empresaName
from django.shortcuts import redirect, render


def produto_insert(request):
    message = ""
    if request.method == "POST":
        produto_nome = request.POST.get("produto_nome")
        insert_doc = {
                      "produto_nome": produto_nome,
                      }
        do_insert_produto(insert_doc)
        message = "Inserido com sucesso!"
    return render(request, "produto_insert.html", {"insert":True,"message":message,})


def produto_control(request):
    produtos=list(do_read_produto_all())
    for produto in produtos:
        produto["id"] = str(produto["_id"])
    return render(request, "produto_control.html", {"produtos":produtos,})

def produto_empresa(request,empresaID):
    empresa = do_read_empresa_by_id(empresaID)
    empresa_name = str(empresa["name"])
    produtos = list(do_read_produto_empresaName(empresa_name))
    for produto in produtos:
        produto_codigo = produto["produto_codigo"] 
        produto_nome = produto["produto_nome"]
        produto_preco = produto["produto_preco"] 
        qtd_minima = produto["qtdmin"] 
        desconto = produto["descmax"] 
        empresa_nome = produto["empresa"] 
        return render(request, "empresa_produto.html", {"produtos":produtos,"produto_codigo":produto_codigo,"produto_nome":produto_nome,"produto_preco":produto_preco,"qtd_minima":qtd_minima,"desconto":desconto,"empresa_nome":empresa_nome})
    


def delete_produto(request,produtoID,view=None):
    do_delete_produto(produtoID)
    response = redirect("empresa:produto_control")
    return response

