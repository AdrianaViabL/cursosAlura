$('#btPlacar').click(mostraPlacar)
$('#btnSync').click(sincronizaPlacar)

function inserePlacar(){
    var tabela = $('.placar').find('tbody')
    var usuario = 'Adriana'
    var nPalavras = $('#contPalavras').text()
    //dessa forma esta sendo criado uma string que sera adicionada dentro da tabela, mas precisamos de um e
    //var btnRemover = '<a href=""><i class="material-icons">delete</i></a>'

    var linha = novaLinha(usuario, nPalavras)
    linha.find('.btnRemover').click(removeLinha)

    tabela.prepend(linha) 
    $('.placar').slideDown(500)
    scrollDown($('.placar'))  
}

function scrollDown(tag){
    posicaoTag = tag.offset().top
    console.log(tag)
    $('html').animate(
    {
        scrollTop: posicaoTag+'px'//usando a posição da tag como parametro para a função animate
    },1000)
}



function novaLinha(usuario, nPalavras){
    var linha = $('<tr>')//criando o elemento tr do HTML
    var colUser = $('<td>').text(usuario)
    var colPalav = $('<td>').text(nPalavras)
    var colRemover = $('<td>')

    var link = $('<a>').addClass('btnRemover').attr('href', '#')
    var icone = $('<i>').addClass('small material-icons').text('delete')

    link.append(icone)
    colRemover.append(link)
    linha.append(colUser, colPalav, colRemover)

    return linha
}
function removeLinha(event){
        event.preventDefault()
        var linha = $(this).parent().parent()
        linha.fadeOut(1000)
        setTimeout(function(){
            linha.remove()
        }, 1000)
        //linha.fadeOut(function(){linha.remove()}) <- outra forma de remover o elemento depois de ter o efeito de sumir
}

function mostraPlacar(){
    $('.placar').stop().slideToggle()
}

function sincronizaPlacar(){
    var placar = []
    var linhas = $('tbody > tr')
    linhas.each(function(){
        var usuario = $(this).find('td:nth-child(1)').text()//procurando no primeiro td dentro do tr
        var qtdPalavras = $(this).find('td:nth-child(2)').text()

        var score = {
            usuario: usuario,
            pontos: qtdPalavras
        }
        placar.push(score)
    })
    
    //criando o objeto para ser enviado pelo AJAX
    var dados = {
        placar: placar
    }
    $.post('http://localhost:3000/placar', dados, function(){
        console.log('deu certo O.o')
    })
}
