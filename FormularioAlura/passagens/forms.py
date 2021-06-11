from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classes


class PassagemForms(forms.Form):
    origem = forms.CharField(label='origem', max_length=100)
    destino = forms.CharField(label='destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today())
    classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipos_de_classes)
    informacoes = forms.CharField(label='Informações extras', max_length=200, widget=forms.Textarea(), required=False)
    email = forms.EmailField(label='Email', max_length=100)

