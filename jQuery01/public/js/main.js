//Para rodar o servidor com o nodejs (depois de instalar o nodejs), va na pasta do servidor e no terminal digite 'npm start'

//var frase = jQuery('.frase') //é a mesma coisa que usar o $ para acessar a informação dentro do DOM
var tmpInicial = $('#temDigita').text()
var campo = $('.cDigitacao')
var btnReiniciar = $('#btReiniciar')
var btntxtAleatorio = $('#btnFrase')
var btnFraseID = $('#btnFraseID')


//um atalho para o $(document).ready(function(){})
$(function(){//deixando todas as chamadas de funções para depois de a pagina ter sido inicializada
    atualizaContadores()
    atualizaTamFrases()
    inicializaContadores()
    contRegressiva()
    btnReiniciar.click(reiniciaJogo)
    $('table').find('.btnRemover').click(removeLinha)//precisou dessa linha pros dados do HTML serem apagados O.o
    atualizaPlacar()
    $('#usuarios').selectize({
        create: true,
        sortField: 'text'
    })
})

function atualizaTamFrases(){
    var frase = $('.frase').text()
    var tamFrase = frase.split(/\S+/).length -1
    var listFrase = $('#tamFrase')
    listFrase.text(tamFrase)
}
//$('.cDigitacao').click(function(){}) = uma segunda forma de acessar os dados dentro da textarea
function atuTempoInicial(tempo){
    tmpInicial = tempo
    $('#temDigita').text(tempo)
}

function atualizaContadores(){
    campo.on('input', function(){
        var conteudo = campo.val().trim()//pegando o valor dos input dos usuarios
        var qtdPalavras = conteudo.split(/\S+/).length -1//expressao regular que procura todo tipo de espaço
        $('#contPalavras').text(qtdPalavras)
        $('#contCaracteres').text(conteudo.length)
    })
}

function contRegressiva(){
    btnReiniciar.attr('disabled', true)
    campo.one('focus', function(){//focus - detecta quando o campo entra em 'foco'(é acessado via click ou com o uso do TAB)
        btntxtAleatorio.attr('disabled', true)
        btnFraseID.attr('disabled', true)
        var tempoFim = $("#temDigita").text()
        var cronID = setInterval(function(){
            tempoFim--
            $('#temDigita').text(tempoFim)
            campo.attr('')
            if (tempoFim < 1 ){
                clearInterval(cronID)
                fimJogo()
            }
        }, 1000)
    })
}

function fimJogo(){
    campo.attr('disabled', true)//adicionando um valor na tag textarea
    campo.toggleClass('desativa-fundo-cor')
    btnReiniciar.attr('disabled', false)
    btntxtAleatorio.attr('disabled', false)
    btnFraseID.attr('disabled', false)
    inserePlacar()
}

function inicializaContadores(){
    campo.on('input', function(){   
        var frase = $('.frase').text()
        var digitado = campo.val()
        var comparavel = frase.substr(0, digitado.length)

        if(digitado == comparavel){
            campo.removeClass('borda-errado')
            campo.addClass('borda-correto')
        }else{
            campo.removeClass('borda-correto')
            campo.addClass('borda-errado')
        }
    })
}


function reiniciaJogo(){
    campo.attr('disabled', false)
    campo.val('')
    campo.toggleClass('desativa-fundo-cor')
    campo.removeClass('borda-correto')
    campo.removeClass('borda-errado')
    $("#contCaracteres").text(0)
    $("#contPalavras").text(0)
    $('#temDigita').text(tmpInicial)
    contRegressiva()
    
}

