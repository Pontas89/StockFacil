const pesquisa = document.querySelector("#pesquisa-produto");
const linhas = document.querySelectorAll("tbody tr[data-status]");
const filtroStatus = document.querySelector("#filtro-status");
const pesquisaMovimentacao = document.querySelector("#pesquisa-movimentacao");
const filtroTipo =document.querySelector("#filtro-tipo");
const linhasMovimentacao = document.querySelectorAll("tbody tr[data-tipo]");

//Filtro -> movimentacoes
function filtrarMovimentacoes() {
    if (!pesquisaMovimentacao || ! filtroTipo){
        return;
    }

    const texto = pesquisaMovimentacao.value.toLowerCase();
    const tipoSelecionado = filtroTipo.value;

    linhasMovimentacao.forEach(function(linha) {
        const nome = linha.cells[0].textContent.toLowerCase();
        const tipo = linha.getAttribute("data-tipo");

        if(nome.includes(texto) && (tipoSelecionado === "" || tipo === tipoSelecionado)) {

            linha.style.display = "";
        }
        else {
            linha.style.display = "none";
        }

    });
}

if (pesquisaMovimentacao) {
    pesquisaMovimentacao.addEventListener("input", filtrarMovimentacoes);
}

if (filtroTipo) {
    filtroTipo.addEventListener("change", filtrarMovimentacoes);
}

//Filtro -> produtos
function filtrarProdutos() {

    if(!pesquisa || !filtroStatus) {
        return;
    }

    const texto = pesquisa.value.toLowerCase();
    const statusSelecionado = filtroStatus.value;

    linhas.forEach(function (linha) {
        const nome = linha.cells[0].textContent.toLowerCase();
        const statusProduto = linha.getAttribute("data-status");

        if (nome.includes(texto) && (statusSelecionado === "" || statusProduto === statusSelecionado)) {
            linha.style.display = "";
        }

        else {
            linha.style.display = "none";
        }
    });
}

if (pesquisa) {
    pesquisa.addEventListener("input", function() {
        filtrarProdutos();
    });
}

if (filtroStatus) {
    filtroStatus.addEventListener("change", function() {
        filtrarProdutos();
    });
}

//Alternancia de tema
const botaoTema = document.getElementById('tema-toggle');

//salvar tema
const temaSalvo = localStorage.getItem('tema') || 'light';

document.documentElement.setAttribute('data-theme', temaSalvo);

//atualizar icone
function atualizarIconeTema() {
    if (!botaoTema) return;

    const temaAtual = document.documentElement.getAttribute('data-theme');

    if(temaAtual === 'dark') {
        botaoTema.innerHTML = '<i class="bi bi-sun"></i>';
    }
    else {
        botaoTema.innerHTML = '<i class="bi bi-moon"></i>';
    }
}

atualizarIconeTema();

if (botaoTema) {
    botaoTema.addEventListener('click', function() {
        const temaAtual = document.documentElement.getAttribute('data-theme');

        let novoTema;

        if(temaAtual === 'dark') {
            novoTema = 'light';
        }

        else {
            novoTema = 'dark';
        }

        document.documentElement.setAttribute('data-theme', novoTema);

        localStorage.setItem('tema', novoTema);

        atualizarIconeTema();
    });
}
