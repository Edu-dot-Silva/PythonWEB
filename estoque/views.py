from django.shortcuts import render,redirect,get_object_or_404

from .models import Estoque

from datetime import datetime


# Create your views here.

def index(request):
    return render (request,'index_estoque.html')

def cadastro(request):
    return render(request,'cadastro_estoque.html')

def lista(request):
    lista_produtos = Estoque.objects.all()
    
    return render(request,'lista_estoque.html',{'lista_produtos':lista_produtos})

def criar_produto(request):
    nome_produto = request.POST['nome_produto']
    descricao = request.POST['descricao_produto']
    preco = request.POST['preco_produto']
    max_estoque = request.POST['max_produto']
    min_estoque = request.POST['min_produto']
    
    produto = Estoque.objects.create(nome_produto=nome_produto,descricao=descricao,preco=preco,max_estoque=max_estoque,min_estoque=min_estoque)
    
    produto.save()
    
    return redirect('index_estoque')

def excluir_produto(request,id_produto):
    produto = get_object_or_404(Estoque,pk=id_produto)
    
    produto.delete()
    
    return redirect('index_estoque')

def editar_produto(request,id_produto):
    produto= get_object_or_404(Estoque,pk=id_produto)
    
    return render(request,'atualizar_estoque.html',{'dados_produto': produto})

def atualizar_produto(request):
    
    id_produto = request.POST["id"]
    
    produto = Estoque.objects.get(pk = id_produto)
    
    produto.nome_produto = request.POST["nome_produto"]
    produto.descricao = request.POST["descricao_produto"]
    produto.preco = request.POST["preco_produto"]
    produto.max_estoque = request.POST["max_produto"]
    produto.min_estoque = request.POST["min_produto"]
    
    produto.save()
    
    return redirect('index_estoque')