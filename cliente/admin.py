from django.contrib import admin
from .models import Clientes
# importando os clientes da model
from .models import Estoque

admin.site.register(Clientes)
# registrando a tabela de clientes no admin do django


admin.site.register(Estoque)
