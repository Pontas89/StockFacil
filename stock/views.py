from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy ## Transforma o name da rota em URL. É "lazy" porque as rotas ainda não existem quando a classe é lida.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from stock.forms import PersonForm
from stock.models import Person, Course  # troque courses pelo nome do seu app


class PersonListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "stock.view_person"
    model = Person ## tabela usada
    template_name = "pessoas/pessoa_list.html"  ## template da tabela
    context_object_name = "object_list" ## Nome do registro no template
    paginate_by = 10 ## paginação da lista

class PersonCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "stock.add_person"
    model = Person
    form_class = PersonForm ## PersonForm (formulário) da class nos forms.py
    template_name = "pessoas/pessoa_form_create.html"
    success_url = reverse_lazy("stock:pessoa_list")

class PersonUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "stock.change_person"
    model = Person
    form_class = PersonForm ## Usa o formulário PersonForm criado em forms.py para preencher os campos que será atualizado
    # troque courses pelo nome do seu app
    template_name = "pessoas/pessoa_form_update.html"
    context_object_name = "usuario" ## Nome do registro no template
    success_url = reverse_lazy("stock:pessoa_list")

class PersonDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "stock.delete_person"
    model = Person 
    template_name = "pessoas/pessoa_confirm_delete.html"  ## course_confirm_delete.html: Página que pergunta "tem certeza?". Abrir o link não apaga nada, só o post do botão apaga.
    context_object_name = "pessoa_deletada"
    success_url = reverse_lazy("stock:pessoa_list")

    ## Sem form_class: Excluir não tem campos para preencher, então não usa formulário.