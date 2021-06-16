def origem_destino_iguais(origem, destino, lista_erros):
    if origem == destino:
        lista_erros['destino'] = 'Origem e destino não podem ser iguais'


def tem_numero(valor_campo, nome_campo, lista_erros):
    if any(char.isdigit() for char in valor_campo):
        lista_erros[nome_campo] = f'{nome_campo} inválida: não pode incluir numero'


def valida_data(data_ida, data_volta, data_pesquisa, lista_erro):
    """Valida se a data de ida é maior que a data de volta e a data de ida é menor que a data atual"""
    if data_ida > data_volta:
        lista_erro['data_volta'] = 'Data de volta não pode ser maior que a data de ida'
    if data_ida < data_pesquisa:
        lista_erro['data_ida'] = 'Data de ida não pode ser menor do que a data de hoje'
