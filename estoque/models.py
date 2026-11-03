from django.db import models
from stock.models import Produto

class Movimentacao(models.Model):

    TIPOS = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPOS) #para entrada ou saida
    quantidade = models.IntegerField() #armazenar p/ entrada ou saida
    data = models.DateTimeField(auto_now_add=True)