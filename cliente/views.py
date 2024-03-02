from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# importando o http response do django

# as defs na view sempre sera uma pagina nova

# def index(request):
#     return HttpResponse("<h1>Hello World</h1>")
# criando um função que retorna um h1
# para funcionar precisa ser criado uma rota

from .models import Clientes

from .models import Estoque

# retornando o html do template
def index(request):
    return render(request,'index.html')


def cadastro(request):
    return render(request,'cadastro.html')

def listar(request):
    lista_clientes = Clientes.objects.all()
    # definindo a variavel que vai receber todos os clientes    
    return render (request,'listar.html' , {'lista':lista_clientes})
# criando a função que vai renderizar o listar.html
# chamando a variavel que esta armazenando a lista de clientes

def estoque(request):
    estoque = Estoque.objects.all()
    
    return render (request,'estoque.html',{'estoque':estoque})
