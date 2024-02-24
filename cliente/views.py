from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# importando o http response do django

# as defs na view sempre sera uma pagina nova

# def index(request):
#     return HttpResponse("<h1>Hello World</h1>")
# criando um função que retorna um h1
# para funcionar precisa ser criado uma rota

# retornando o html do template
def index(request):
    return render(request,'index.html')


def cadastro(request):
    return render(request,'cadastro.html')