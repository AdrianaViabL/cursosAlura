from django.shortcuts import render
from passagens.forms import PassagemForms


def index(request):
    form = PassagemForms()
    contexto = {'form':form}
    return render(request, 'index.html', contexto)


def review_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        if form.is_valid():
            contexto = {'form':form}
            return render(request, 'consulta.html', contexto)
        else:
            contexto = {'form':form}
            return render(request, 'index.html', contexto)