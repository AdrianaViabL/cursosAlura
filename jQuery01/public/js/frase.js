$('#btnFrase').click(fraseAleatoria)

function fraseAleatoria(){//requisição AJAX para pegar parametros no servidor no caminho informado
    $.get('http://localhost:3000/frases', pegaFrase)
    .fail(function() {
        $('#erro').toggle()
        setTimeout(function(){
            $('#erro').toggle()
        }, 1500)
        
    })

}

function pegaFrase(data){
    var frase = $('.frase')
    var numAleatorio = Math.floor(Math.random() * data.length)//pegando um numero aleatorio baseado na quantidade de valores dentro do array 
    frase.text(data[numAleatorio].texto)
    atualizaTamFrases()
    atuTempoInicial(data[numAleatorio].tempo)
}
