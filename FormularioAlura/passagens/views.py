from django.shortcuts import render
from passagens.forms import PassagemForms, PessoaForms


def index(request):
    form = PassagemForms()
    pessoa_form = PessoaForms()
    contexto = {'form': form, 'pessoa_form': pessoa_form}
    return render(request, 'index.html', contexto)


def review_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        pessoa_form = PessoaForms(request.POST)
        if form.is_valid():
            contexto = {'form':form, 'pessoa_form': pessoa_form}
            return render(request, 'consulta.html', contexto)
        else:
            contexto = {'form':form, 'pessoa_form': pessoa_form}
            return render(request, 'index.html', contexto)