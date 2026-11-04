from django.urls import path
from vendas.views import ListarVenda, VendaDeletar, VendaEditar, CriarVenda

app_name = "vendas"

urlpatterns = [
    path('list/', ListarVenda.as_view(), name='vendas_list'),
     path('criar/', CriarVenda.as_view(), name='vendas_create'),
     path('editar/<int:pk>/', VendaEditar.as_view(), name='vendas_update'),
     path('deletar/<int:pk>/', VendaDeletar.as_view(), name='vendas_delete'),
]
