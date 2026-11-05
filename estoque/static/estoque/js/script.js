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
