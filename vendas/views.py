from vendas.forms import VendaForm
from vendas.models import Venda
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class ListarVenda(ListView):
    model = Venda
    template_name = "vendas/vendas_list.html"
    context_object_name = "vendas"
    paginate_by = 10

class CriarVenda(CreateView):
    model = Venda
    form_class = VendaForm
    template_name = "vendas/vendas_create.html"
    success_url = reverse_lazy("vendas:vendas_list")

class VendaEditar(UpdateView):
    model = Venda
    form_class = VendaForm
    template_name = "vendas/vendas_update.html"
    context_object_name = "vendas"
    success_url = reverse_lazy("vendas:vendas_list")

class VendaDeletar(DeleteView):
    model = Venda
    template_name = "vendas/vendas_delete.html"
    context_object_name = "vendas"
    success_url = reverse_lazy("vendas:vendas_list")

