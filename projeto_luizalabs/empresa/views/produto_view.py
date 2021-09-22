from projeto_luizalabs.core.web.business.empresa_business import do_read_empresa_all, do_read_empresa_by_id
from projeto_luizalabs.core.web.business.produto_business import do_delete_produto, do_insert_produto, do_read_produto_all, do_read_produto_by_id, do_read_produto_empresaName
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
    produtos = empresa["produtos"]
    print(produtos)
    for produto in produtos:
        produto["produto_nome"] = do_read_produto_by_id(produto["id_produto"])["produto_nome"]
    return render(request, "empresa_produto.html", {"produtos": produtos,"empresa":empresa})
    


def delete_produto_empresa(request,produtoID,view=None):
    empresa=do_read_empresa_by_id(id_empresa)
    for id_produto in produtos:
        for produto in empresa["produtos"]:
            if id_produto == produto["id_produto"]:
                empresa["produtos"].remove(produto)
        inserted_id = do_update_empresa(id_empresa,empresa)
