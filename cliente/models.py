from django.db import models

from datetime import datetime

# Create your models here.

class Clientes(models.Model):
    primeiro_nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    status = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now,blank=True)
    # criando a classe base de dados dos clientes que virao do banco de dados

    # pode alterar os atributos do banco mas tem que rodar os comandos no terminal
    # python manage.py makemigrations
    # python manage.py migrate
    
    # para atualizar o banco,em aula foi alterado o tamanho do email e o datetime do created e do updated
