from django.db import models
from django.contrib.auth.models import User
from stock.models import Produto 

class Venda(models.Model):
    METODOS = [
        ('Pix', 'Pix'),
        ('Cartão', 'Cartão'),
        ('Dinheiro', 'Dinheiro'),
    ]
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    forma_pagamento = models.CharField(max_length=50, choices=METODOS)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    finalizada = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Venda {self.id} - Cliente: {self.cliente.username} - Total: R${self.valor_total}"  
    
class Carrinho(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='carrinho')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
