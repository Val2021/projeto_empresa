
from projeto_luizalabs.core.web.databases.produtoDB import delete_produto, insert_produto, read_produto_all, read_produto_by_id, read_produto_empresaName, update_produto



def do_insert_produto(insert_doc):
    return  insert_produto(insert_doc)


def do_read_produto_empresaName(empresa):
    return read_produto_empresaName(empresa)


def do_delete_produto(produtoID):
    return delete_produto(produtoID)

def do_read_produto_all():
    return read_produto_all()
    


def do_read_produto_by_id(produtoID):
    return read_produto_by_id(produtoID)


def do_update_produto(produtoID, update_doc):
    return update_produto(produtoID, update_doc)

   