from projeto_luizalabs.core.web.business.empresa_business import do_insert_empresa, do_read_empresa_all
from django.shortcuts import render



def empresa_control(request):
    empresas=list(do_read_empresa_all())
    for empresa in empresas:
        empresa["id"] = str(empresa["_id"])
    return render(request, "empresa_control.html", {"empresas":empresas,})


def customer_insert(request, _id, positions=None, token=None):
    message = ""
    if request.method == "POST":
        empresa_number = request.POST.get("empresa_number")
        type_empresa = request.POST.get("type_customer")
        cnpj = request.POST.get("cnpj")
        name = request.POST.get("name")
        corporate_name = request.POST.get("corporate_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        insert_doc = {"empresa_number": str(empresa_number),
                      "type_empresa": type_empresa,
                      "cnpj": cnpj,
                      "name": name,
                      "corporate_name":corporate_name,
                      "email":email,
                      "phone": phone}
        do_insert_empresa(insert_doc)
        message = "Inserido com sucesso!"
    return render(request, "empresa_insert.html", {"userID": _id,"insert":True, "message":message,"positions": positions, "token": token})