from django.shortcuts import render

def home(request):
    return render(request, "luizalabs.html")

def dashboard(request):
    return render(request, "luizalabs.html")