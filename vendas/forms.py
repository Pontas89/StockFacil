from django import forms
from vendas.models import Venda

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'forma_pagamento', 'valor_total', 'finalizada']