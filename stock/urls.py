from django.urls import path
from stock.views import PersonListView, PersonCreateView, PersonUpdateView, PersonDeleteView, ProdutoListar, ProdutoCriar, ProdutoEditar, ProdutoDeletar # troque courses pelo nome do seu app

app_name = "stock"


## Estrutura da url:

## name ("apelido") para url que o html vai encontrar

urlpatterns = [
    path("listar/", PersonListView.as_view(), name="pessoa_list"), 
    path("criar/", PersonCreateView.as_view(), name="pessoa_create"),
    path("<int:pk>/editar/", PersonUpdateView.as_view(), name="pessoa_update"),
    path("<int:pk>/deletar/", PersonDeleteView.as_view(), name="pessoa_delete"),
    path("produtos/", ProdutoListar.as_view(), name='produto_listar'),
    path("criar-produto/", ProdutoCriar.as_view(), name='produto_criar'),
    #<int:pk> = Parte variável da URL: o id do curso.
    path("<int:pk>/editar-produto/", ProdutoEditar.as_view(), name='produto_editar'),
    path("<int:pk>/deletar-produto/", ProdutoDeletar.as_view(), name='produto_deletar'),
]
