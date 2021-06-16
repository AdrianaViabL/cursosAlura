from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classes
from passagens.validation import *


class PassagemForms(forms.Form):
    origem = forms.CharField(label='origem', max_length=100)
    destino = forms.CharField(label='destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today())
    classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipos_de_classes)
    informacoes = forms.CharField(label='Informações extras', max_length=200, widget=forms.Textarea(), required=False)
    email = forms.EmailField(label='Email', max_length=100)

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
