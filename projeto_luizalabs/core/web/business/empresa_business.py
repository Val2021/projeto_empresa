
from projeto_luizalabs.core.web.databases.empresaDB import delete_empresa, insert_empresa, read_empresa_all, read_empresa_by_id, update_empresa


def do_insert_empresa(empresa):
    return insert_empresa(empresa)


def do_delete_empresa(empresaID):
    return delete_empresa(empresaID)


def do_read_empresa_all():
    return read_empresa_all()


def do_read_empresa_by_id(empresaID):
    return read_empresa_by_id(empresaID)


def do_update_empresa(id_empresa,empresa):
    return update_empresa (id_empresa,empresa)