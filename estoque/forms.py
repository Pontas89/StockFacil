from django import forms
from .models import Movimentacao

class MovimentacaoForm(forms.ModelForm): #cria um formulario
    class Meta:
        model = Movimentacao
        fields = ['produto', 'tipo', 'quantidade']

        widgets = {
            'produto': forms.Select(attrs={'class': 'form-select'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_quantidade(self):
        quantidade = self.cleaned_data['quantidade']

        if quantidade <= 0:
            raise forms.ValidationError('A quantidade deve ser maior que zero.')
        return quantidade

    def clean_tipo(self):
        tipo = self.cleaned_data['tipo']

        if tipo not in ['entrada', 'saida']:
            raise forms.ValidationError('Tipo de movimentação inválido.')
        return tipo