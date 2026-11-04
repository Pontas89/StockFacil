from django.db import models

# Create your models here.
class Produto(models.Model):
    #CharField = Texto curto, exige max_length.
    nome_produto = models.CharField(max_length=80)
    #PositiveIntegerField = Número inteiro, sem negativos (default=0 define o valor inicial)
    quantidade_produto = models.PositiveIntegerField(verbose_name="Quantidade", default=0)
    preco_produto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço (Un)")

    #Configurações do model, não viram coluna
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["nome_produto"]


    def __str__(self):
        return self.nome_produto