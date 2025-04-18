from django.urls import path
from .views import home, login_view, logout_view, register_view, categoria_list, categoria_detail, departamento_list, departamento_detail, fornecedor_list, fornecedor_detail, bem_list, bem_detail, movimentacao_list, movimentacao_detail,categoria_create, departamento_create, fornecedor_create, bem_create, movimentacao_create, bem_edit

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    
    #LOGIN
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

    #CATEGORIAS
    path('categorias/', categoria_list, name='categoria_list'),
    path('categoria/<int:id>/', categoria_detail, name='categoria_detail'),
    path('categorias/cadastrar/', categoria_create, name='categoria_create'),
    
    #DEPARTAMENTOS
    path('departamentos/', departamento_list, name='departamento_list'),
    path('departamentos/<int:id>/', departamento_detail, name='departamento_detail'),
    path('departamentos/cadastrar/', departamento_create, name='departamento_create'),
    
    #FORNECEDORES
    path('fornecedores/', fornecedor_list, name='fornecedor_list'),
    path('fornecedores/<int:id>/', fornecedor_detail, name='fornecedor_detail'),
    path('fornecedores/cadastrar/', fornecedor_create, name='fornecedor_create'),
    
    #BENS
    path('bens/', bem_list, name='bem_list'),
    path('bens/<int:id>/', bem_detail, name='bem_detail'),
    path('bens/cadastrar/', bem_create, name='bem_create'),
    path('bens/editar/<int:id>/', bem_edit, name='bem_editar'),

    #MOVIMENTACOES
    path('movimentacoes/', movimentacao_list, name='movimentacao_list'),
    path('movimentacoes/<int:id>/', movimentacao_detail, name='movimentacao_detail'),
    path('movimentacoes/cadastrar/', movimentacao_create, name='movimentacao_create'),

]
