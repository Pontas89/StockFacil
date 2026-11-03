from django.shortcuts import render, redirect
from stock.models import Produto
from .forms import MovimentacaoForm
from .models import Movimentacao

def dashboard(request):
    produtos = Produto.objects.all() #busca todos os produtos cadastrados no banco

    total_produtos = produtos.count()

    produtos_disponiveis = produtos.filter(
        quantidade_produto__gt=5 #conta quantos produtos tem maior que 5
    ).count()

    estoque_baixo = produtos.filter(
        quantidade_produto__gt=0,
        quantidade_produto__lte=5 #conta quantos produtos tem menor ou igual a 5
    ).count()

    produtos_esgotados = produtos.filter(
        quantidade_produto=0
    ).count()

    return render(request, 'estoque/dashboard.html', {  #envia os produtos pro HTML
        'produtos': produtos,
        'total_produtos': total_produtos,
        'produtos_disponiveis': produtos_disponiveis,
        'estoque_baixo': estoque_baixo,
        'produtos_esgotados': produtos_esgotados
    })

def movimentacoes(request):
    form = MovimentacaoForm() #formulario VAZIO

    if request.method == 'POST': #se preencheu e clicou em registrar
        form = MovimentacaoForm(request.POST) #ficar dentro de form

        if form.is_valid(): #se são validos
            movimentacao = form.save(commit=False) #salva a movimentacao

            produto = movimentacao.produto #encontra o produto

            #atualizacao
            if movimentacao.tipo == 'saida': #OBS se a saida for maior que o estoque vai ser BLOQUEADA.
                if movimentacao.quantidade > produto.quantidade_produto:
                    form.add_error('quantidade', 'Estoque insuficiente.')

                else:
                    produto.quantidade_produto -= movimentacao.quantidade
                    produto.save()
                    movimentacao.save()
                    return redirect('movimentacoes')

            else:
                produto.quantidade_produto += movimentacao.quantidade
                produto.save()
                movimentacao.save()
                return redirect('movimentacoes')

    movimentacoes = Movimentacao.objects.select_related('produto').order_by('-data') #para buscar o historico, ainda mais quando tem muitos registros (inves de objects.all())

    #enviar informacoes pro HTML e mostrar pro usuario
    return render(request, 'estoque/movimentacoes.html', {
        'form': form,
        'movimentacoes': movimentacoes
    })

def estoque_baixo(request):
    produtos = Produto.objects.filter(
        quantidade_produto__gt=0,
        quantidade_produto__lte=5
    )

    return render(request, 'estoque/estoque_baixo.html', {
        'produtos': produtos
    })
