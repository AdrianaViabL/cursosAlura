//var frase = jQuery('.frase') //é a mesma coisa que usar o $ para acessar a informação dentro do DOM
var tmpInicial = $('#temDigita').text()
var campo = $('.cDigitacao')


//um atalho para o $(document).ready(function(){})
$(function(){//deixando todas as chamadas de funções para depois de a pagina ter sido inicializada
    atualizaContadores()
    atualizaTamFrases()
    contRegressiva()
    $('#btReiniciar').click(reiniciaJogo)
})

function atualizaTamFrases(){
    var frase = $('.frase').text()
    var tamFrase = frase.split(' ').length
    var listFrase = $('#tamFrase').text(tamFrase)
}
//$('.cDigitacao').click(function(){}) = uma segunda forma de acessar os dados dentro da textarea


function atualizaContadores(){
    campo.on('input', function(){
        var conteudo = campo.val().trim()//pegando o valor dos input dos usuarios
        var qtdPalavras = conteudo.split(/\S+/).length -1//expressao regular que procura todo tipo de espaço
        $('#contPalavras').text(qtdPalavras)
        $('#contCaracteres').text(conteudo.length)
    })
}

function contRegressiva(){
    campo.one('focus', function(){//focus - detecta quando o campo entra em 'foco'(é acessado via click ou com o uso do TAB)
        var tempoFim = $("#temDigita").text()
        var cronID = setInterval(function(){
            tempoFim--
            $('#temDigita').text(tempoFim)
            campo.attr('')
            if (tempoFim < 1 ){
                campo.attr('disabled', true)//adicionando um valor na tag textarea
                clearInterval(cronID)
                campo.addClass('desativa-fundo-cor')
            }
        }, 1000)
    })
}

function reiniciaJogo(){
    
    campo.attr('disabled', false)
    campo.val(' ')
    campo.removeClass('desativa-fundo-cor')
    $("#contCaracteres").text(0)
    $("#contPalavras").text(0)
    $('#temDigita').text(tmpInicial)
    contRegressiva()

}

