from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classes
from passagens.validation import *
from passagens.models import Passagem, ClasseViagem, Pessoa


class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data de pesquisa', disabled=True, initial=datetime.today())
    class Meta: #classe responsável por manipular o modelo para gerar o formulário
        model = Passagem
        fields = '__all__'
        labels = {'data_ida': 'Data de ida',
                  'data_volta': 'Data de volta',
                  'informacoes': 'Informações'
                  }

        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker()
        }

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_erros = {}
        tem_numero(origem, 'origem', lista_erros)
        tem_numero(destino, 'destino', lista_erros)
        origem_destino_iguais(origem, destino, lista_erros)
        valida_data(data_ida, data_volta, data_pesquisa, lista_erros)

        if lista_erros:
            for erro in lista_erros:
                mensagem = lista_erros[erro]
                self.add_error(erro, mensagem)
        return self.cleaned_data

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome'] #ele traz todos os campos menos os especificados aqui
