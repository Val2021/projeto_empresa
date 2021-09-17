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
        message = "Inserido com sucesso!"
    print("id",empresaID)
    empresa = do_read_empresa_by_id(empresaID)
    print("empre",empresa)
    empresa["_id"] = str(empresa["_id"])
    empresa["id"] = empresa["_id"]
    return render(request, "empresa_insert.html", { "message":message,"empresa":empresa})

def delete_empresa(request,empresaID,view=None):
    do_delete_empresa(empresaID)
    response = redirect("empresa:empresa_control")
    return response