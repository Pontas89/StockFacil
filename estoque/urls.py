from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('movimentacoes/', views.movimentacoes, name='movimentacoes'),
    path('estoque-baixo/', views.estoque_baixo, name='estoque_baixo'),
]