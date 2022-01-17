from django.urls import path
from .views import *

urlpatterns = [
    path('', produtos_list, name='lista_produtos'),
    path('criar_produto', produtos_create, name='criar_produto'),
    path('editar_produto/<int:pk>', produtos_edit, name='editar_produto'),
    path('apagar_produto/<int:pk>', produtos_delete, name='apagar_produto'),
    path('show_produto/<int:pk>', produtos_show, name='show_produto' ),
    path('marcas', marcas_list, name='lista_marcas'),
    path('criar_marca', marcas_create, name='criar_marca'),
    path('editar_marca/<int:pk>', marcas_edit, name='editar_marca'),
    path('apagar_marca/<int:pk>', marcas_delete, name='apagar_marca'),
    path('marca_produtos_list/<int:pk>', marcas_produtos_list, name='marca_produtos_list'),
    path('criar_categoria', categorias_create, name='criar_categoria'),
    path('editar_categoria/<int:pk>', categorias_edit, name='editar_categoria'),
    path('apagar_categoria/<int:pk>', categorias_delete, name='apagar_categoria'),
    path('categorias', categorias_list, name='lista_categorias'),
    path('categoria_produtos_list/<int:pk>', catetegoria_produtos_list, name='categoria_produtos_list'),
]