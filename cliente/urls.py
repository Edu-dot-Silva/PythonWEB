# refatorando as rotas de cliente

from django.urls import path

from. import views
# ese ponto indica que a views esta nessa pasta do projeto

urlpatterns =[
    path('',views.index,name='index_cliente'),
    # outro metodo
    
    path('cadastro',views.cadastro,name='cadastro_cliente'),
    # definido o apelido das rotas
    
    path('listar',views.listar,name='listar_cliente'),
    # definindo a rota de listar
    # url/def/apelido
    
    path('criar_cliente',views.criar,name='criar_cliente'),
    # criando a rota que cria cliente
    
    path('deleta/cliente/<int:id_cliente>',views.deleta_cliente,name='deleta_cliente'),
    
    path('editar/cliente/<int:id_cliente>',views.editar_cliente,name='editar_cliente'),
    
    path('atualizar_cliente',views.atualizar_cliente,name='atualizar_cliente')
]