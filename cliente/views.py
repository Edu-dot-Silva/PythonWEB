from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

from django.http import HttpResponse
# importando o http response do django

# as defs na view sempre sera uma pagina nova

# def index(request):
#     return HttpResponse("<h1>Hello World</h1>")
# criando um função que retorna um h1
# para funcionar precisa ser criado uma rota

from .models import Clientes



from datetime import datetime
#importando a biblioteca que lida com datas e horas

# retornando o html do template
def index(request):
    return render(request,'index_cliente.html')


def cadastro(request):
    return render(request,'cadastro_cliente.html')

def listar(request):
    lista_clientes = Clientes.objects.all()
    # definindo a variavel que vai receber todos os clientes    
    return render (request,'listar_cliente.html' , {'lista':lista_clientes})
# criando a função que vai renderizar o listar.html
# chamando a variavel que esta armazenando a lista de clientes


def criar(request):
    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    email = request.POST['email']
    # criando a função que vai pegar os dados digitados nos inputs

    cliente = Clientes.objects.create(primeiro_nome = nome, sobrenome = sobrenome, email = email, status = 1)
    # atribuindo os valores nos inputs aos campos do banco de dados, tudo dentro de uma variavel
    
    cliente.save()
    # salvando no banco
    
    return redirect('index_cliente')
    # esse comando retorna o usuario para a pagina inicial depois que salvar
    
def deleta_cliente(request,id_cliente):
    cliente = get_object_or_404(Clientes,pk=id_cliente)
        
    cliente.delete()
        
    return redirect('index_cliente')


def editar_cliente(request,id_cliente):
    cliente = get_object_or_404(Clientes,pk=id_cliente)
    
    return render(request,'atualizar_cliente.html',{'dados_cliente': cliente})

def atualizar_cliente(request):
    
    id_cliente = request.POST["id"]

    cliente = Clientes.objects.get(pk = id_cliente)
    
    cliente.primeiro_nome = request.POST["nome"]
    cliente.sobrenome = request.POST["sobrenome"]
    cliente.email = request.POST["email"]
    
    cliente.save()
    
    return redirect('index_cliente')