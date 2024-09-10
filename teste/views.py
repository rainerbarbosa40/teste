from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "teste/index.html")


def pensamentos(request):
    return render(request, "teste/pensamentos.html")
  







# Create your views here.
