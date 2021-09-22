from django.shortcuts import render

def home(request):
    return render(request, "base.html")

def dashboard(request):
    return render(request, "luizalabs.html")