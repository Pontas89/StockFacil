console.log("JavaScript conectado!");
let carrinho = [];  /* lista carrinho vazia para armazenar os produtos */
const botoes = document.querySelectorAll(".btn-adicionar"); /* seleciona todos os botões com a classe btn-adicionar e armazena na variável botoes */
const listaCarrinho = document.getElementById("carrinho-lista"); /* seleciona o elemento com o id carrinho-lista e 
armazena na variável listaCarrinho, feito para listar com o uso do ul */
let totalCompra = document.getElementById("total-compra"); /* seleciona o elemento com o id total-compra e
armazena na variável totalCompra, feito para mostrar o total da compra */

botoes.forEach(function(botao){
    botao.addEventListener("click", function(evento){
    const id = botao.dataset.id;
    const nome = botao.dataset.nome;
    const preco = Number(botao.dataset.preco)
    adicionarAoCarrinho(id, nome, preco);
})
})

function adicionarAoCarrinho(id, nome, preco) {
    let encontrar_produto = carrinho.find(function(produto){
        return produto.id === id;
    })
    if (encontrar_produto) {
        encontrar_produto.quantidade += 1;
    }
    else {
        let produto = {}; /* Cria um objeto vazio para armazenar as informações do parâmetro no produto */
        produto.id = id;
        produto.nome = nome;
        produto.preco = preco; 
        produto.quantidade = 1;
        carrinho.push(produto);
        
    }
    atualizarCarrinho();
}

function atualizarCarrinho(){
    listaCarrinho.innerHTML = "";
    let total = 0;
    carrinho.forEach(function(produto){
        listaCarrinho.innerHTML += `<li>${produto.nome} - R$ ${produto.preco} | Quantidade: ${produto.quantidade}</li>`; /* produto.campo é o objeto com o campo criado */
        listaCarrinho.innerHTML += `<button class = "btn-remover" data-id="${produto.id}">Remover</button>`;
        total += produto.preco * produto.quantidade;
    })

    const botoesRemover = document.querySelectorAll(".btn-remover");

    botoesRemover.forEach(function(botao) {
        botao.addEventListener("click", function() {
            const id = botao.dataset.id;
            removerDoCarrinho(id);
        });
    });
    
    totalCompra.innerHTML = `Total: R$ ${total.toFixed(2)}`;
}

function removerDoCarrinho(id) {
    let novoCarrinho = carrinho.filter(function(produto){ /* Cria uma nova lista de produtos, filtrando os produtos que não possuem o id do produto a ser removido */
        return produto.id !== id;
    })
    carrinho = novoCarrinho; /* Atualiza a lista do carrinho com os produtos restantes após remover o produto */
    atualizarCarrinho(); /* Atualiza a lista do carrinho após remover o produto */
}