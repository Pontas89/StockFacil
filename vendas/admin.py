from django.contrib import admin
from vendas.models import Venda, Carrinho
# Register your models here.

class CarrinhoInline(admin.TabularInline):
    model = Carrinho
    extra = 1

class VendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'forma_pagamento', 'valor_total', 'finalizada','data']
    inlines = [CarrinhoInline]

admin.site.register(Venda, VendaAdmin)

