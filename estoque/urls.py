from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index_estoque'),
    
    path('cadastro',views.cadastro,name='cadastro'),
    path('lista',views.lista,name='lista'),
    
    path('criar_produto',views.criar_produto,name='criar_produto'),

    path('excluir/produto/<int:id_produto>',views.excluir_produto,name='excluir_produto'),
    
    path('editar/produto/<int:id_produto>',views.editar_produto,name='editar_produto'),
    
    path('atualizar_produto',views.atualizar_produto,name='atualizar_produto')    

]