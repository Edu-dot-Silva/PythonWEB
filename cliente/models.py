from django.db import models

# Create your models here.

class Clientes(models.Model):
    primeiro_nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.CharField(max_length=10)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # criando a classe base de dados dos clientes que virao do banco de dados
    

class Estoque(models.Model):
    nome_produto = models.CharField(max_length=10)
    descricao = models.CharField(max_length=255)
    preco = models.FloatField()
    max_estoque = models.IntegerField()
    min_estoque = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
