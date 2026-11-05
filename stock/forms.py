from django import forms
from stock.models import Person  # troque courses pelo nome do seu app
from django import forms 
from stock.models import Produto

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            "first_name",
            "last_name"
        ]

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        #fields =  Campos exibidos no formulário, na ordem da lista. Os rótulos vêm do verbose_name de cada campo.
        fields= ["nome_produto", "quantidade_produto", "preco_produto", "imagem_produto"]
