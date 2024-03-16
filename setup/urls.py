from django.contrib import admin
from django.urls import path,include
# o include é necessario para importar a rota de cliente


urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('',include('usuario.urls')),
    # path('',include('cliente.urls')),
    # declarando a url do cliente
    
    path('clientes/',include('cliente.urls')),
    
    path('estoque/',include('estoque.urls'))
    
]
