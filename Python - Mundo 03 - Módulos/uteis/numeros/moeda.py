# noinspection NonAsciiCharacters
def aumentar(preço=0, taxa=0, forma=False):
    """"→ Calcula o aumento de um determinado preço,
     retornando o resultado com formatação opcional
    :param preço: O preço/valor que se quer reajustar
    :param taxa: A porcentagem da adição
    :param forma: A formatação em forma monetária"""
    resp = preço + (preço * taxa / 100)
    return resp if forma is False else moeda(resp)


# noinspection NonAsciiCharacters
def diminuir(preço=0, taxa=0, forma=False):
    """"→ Calcula a diminuição de um determinado preço,
    retornado o resultado com formatação opcional
    :param preço: O preço/valor que se quer reajustar
    :param taxa: A porcentagem da subtração
    :param forma: A formatação em forma monetária"""
    resp = preço + (preço * taxa / 100)
    return resp if forma is False else moeda(resp)


# noinspection NonAsciiCharacters
def metade(preço=0, forma=False):
    """"→ Calcula a metade de um número.
    :param preço: O preço/valor que se quer reajustar
    :param forma: A formatação em forma monetária"""
    resp = preço // 2
    return resp if forma is False else moeda(resp)


# noinspection NonAsciiCharacters
def dobro(preço=0, forma=False):
    """"→ Calcula o dobro de um número.
    :param preço: O preço/valor que se quer reajustar
    :param forma: A formatação em forma monetária"""
    resp = preço * 2
    return resp if forma is False else moeda(resp)


def moeda(preço, monetário='R$'):
    """"→ Retorna uma str formatada em forma monetária.
    :param preço: O preço/valor que será formatado
    :param monetário: O str em forma monetária"""
    return f'{monetário}{preço:>.2f}'.replace('.', ',')


def resumo(preço, mais=int(), menos=int()):
    # noinspection PyArgumentList
    print('~~~' * 20)
    print('Resumo do Valor'.center(60))
    print('~~~' * 20)
    print(f'Preço analisado:    R${preço}')
    print(f'Dobro do preço:  \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{mais}% de aumento:  \t{aumentar(preço, mais, True)}')
    print(f'{menos}% de redução:  \t{diminuir(preço, menos, True)}')
    print('~~~' * 20)