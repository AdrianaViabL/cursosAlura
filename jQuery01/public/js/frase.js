$('#btnFrase').click(fraseAleatoria)
$('#btnFraseID').click(buscaFrase)

function fraseAleatoria(){//requisição AJAX para pegar parametros no servidor no caminho informado
    $('#spinner').toggle()
    $.get('http://localhost:3000/frases', pegaFrase)
    .fail(function() {
        $('#erro').toggle()
        setTimeout(function(){
            $('#erro').toggle()
        }, 1500)
        
    })
    .always(function(){
        $('#spinner').toggle()
    })
}

function pegaFrase(data){
    var frase = $('.frase')
    var numAleatorio = Math.floor(Math.random() * data.length)//pegando um numero aleatorio baseado na quantidade de valores dentro do array 
    frase.text(data[numAleatorio].texto)
    atualizaTamFrases()
    atuTempoInicial(data[numAleatorio].tempo)
}

function buscaFrase(){
    $('#spinner').toggle()
    var fraseId = $('#fraseID').val()
    var dados = {id: fraseId}
    $.get('http://localhost:3000/frases', dados,trocaFrase)
    .fail(function(){
        $('#erro').toggle()
        setTimeout(function(){
            $('#erro').toggle()
        }, 1500)
    }).always(function(){
        $('#spinner').toggle()
    })
}

function trocaFrase(data){
    var frase = $('.frase')
    frase.text(data.texto)
    atualizaTamFrases()
    atuTempoInicial(data.tempo)
}