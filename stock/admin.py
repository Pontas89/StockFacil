from django.contrib import admin

# Register your models here.

from django.contrib import admin
from stock.models import Person, Course, Produto  # troque courses pelo nome do seu app


class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    search_fields = ("first_name", "last_name")


class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher", "workload", "period")
    search_fields = ("name",)
    list_filter = ("teacher", "period")
    
class ProdutoAdmin(admin.ModelAdmin):
    #list_display = Colunas exibidas na listagem
    list_display = ('nome_produto', 'quantidade_produto', 'preco_produto')
    search_fields = ('nome_produto',)
    list_filter = ('quantidade_produto',)
    ordering = ('nome_produto',)

admin.site.register(Person, PersonAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Produto, ProdutoAdmin)




