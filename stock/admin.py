from django.contrib import admin
from stock.models import Produto 
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    #list_display = Colunas exibidas na listagem
    list_display = ('nome_produto', 'quantidade_produto', 'preco_produto')
    search_fields = ('nome_produto',)
    list_filter = ('quantidade_produto',)
    ordering = ('nome_produto',)

admin.site.register(Produto, ProdutoAdmin)