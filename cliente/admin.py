from django.contrib import admin
from .models import Clientes
# importando os clientes da model


admin.site.register(Clientes)
# registrando a tabela de clientes no admin do django



