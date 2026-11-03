# Create your views here.
from django.shortcuts import render
from stock.models import Produto
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from stock.forms import ProdutoForm
from django.urls import reverse_lazy


class ProdutoListar(ListView):
    model = Produto
    template_name = "stock/produto_stock.html"
    context_object_name = "produtos"
    paginate_by = 10

class ProdutoCriar(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name ="stock/produto_form.html"
    success_url = reverse_lazy("stock:produto_listar")

class ProdutoEditar(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "stock/produto_update.html"
    #Nome do registro no template: {{ course }},
    context_object_name = "produto"
    success_url = reverse_lazy("stock:produto_listar")

class ProdutoDeletar(DeleteView):
    model = Produto
    template_name = "stock/produto_deletar.html"
    context_object_name = "produto"
    success_url = reverse_lazy("stock:produto_listar")
    