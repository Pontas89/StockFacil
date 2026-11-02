from django.urls import path
from stock.views import PersonListView, PersonCreateView, PersonUpdateView, PersonDeleteView  # troque courses pelo nome do seu app

app_name = "stock"


## Estrutura da url:

## name ("apelido") para url que o html vai encontrar

urlpatterns = [
    path("listar/", PersonListView.as_view(), name="pessoa_list"), 
    path("criar/", PersonCreateView.as_view(), name="pessoa_create"),
    path("<int:pk>/editar/", PersonUpdateView.as_view(), name="pessoa_update"),
    path("<int:pk>/deletar/", PersonDeleteView.as_view(), name="pessoa_delete")
]
