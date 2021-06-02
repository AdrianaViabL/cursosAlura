from django import forms

class PassagemForms(forms.Form):
    origem = forms.CharField(label='origem', max_length=100)
    destino = forms.CharField(label='destino', max_length=100)
    data_ida = forms.DateField(label='Ida')
    data_volta = forms.DateField(label='Volta')