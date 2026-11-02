from django.urls import path
from stock.views import ProdutoListar, ProdutoCriar, ProdutoEditar, ProdutoDeletar

app_name = 'stock'
urlpatterns = [
    path("produtos/", ProdutoListar.as_view(), name='produto_listar'),
    path("criar/", ProdutoCriar.as_view(), name='produto_criar'),
    #<int:pk> = Parte variável da URL: o id do curso.
    path("<int:pk>/editar/", ProdutoEditar.as_view(), name='produto_editar'),
    path("<int:pk>/deletar/", ProdutoDeletar.as_view(), name='produto_deletar'),
] 