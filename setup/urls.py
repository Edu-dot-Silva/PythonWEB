from django.contrib import admin
from django.urls import path,include
# o include é necessario para importar a rota de cliente


from cliente import views
# outro metodo de importar as views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    # path('',include('cliente.urls')),
    # declarando a url do cliente
    
    
    path('',views.index,name='index'),
    # outro metodo
    
    path('cadastro',views.cadastro,name='cadastro')
]
