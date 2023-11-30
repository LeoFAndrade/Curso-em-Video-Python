# noinspection NonAsciiCharacters,PyArgumentList
def resumo(preço, mais, menos):
    # noinspection PyArgumentList
    mais = int
    menos = int
    print('~~~' * 20)
    print('Resumo do Valor')
    print('~~~' * 20)
    print(f'Preço analisado    {preço}')
    print(f'Dobro do preço:    {dobro(preço), True}')
    print(f'Metade do preço:    {metade(preço, True)}')
    print(f'{mais}% de aumento: {aumentar(preço, mais, True)}')
    print(f'{menos}% de redução {diminuir(preço, menos, True)}')


na = float(input('Digite um número'))
print(resumo(na, 50, 10))


# noinspection NonAsciiCharacters
def aumentar(preço=0, taxa=0, sit=False):
    """"→ Adiciona o valor da porcentagem sobre um número"""
    resp = preço + (preço * taxa / 100)
    if sit:
        return moeda(resp)
    else:
        return resp


# noinspection NonAsciiCharacters
def diminuir(preço=0, taxa=0, sit=False):
    """"→ Subtrai o valor da porcentagem sobre um número"""
    resp = preço + (preço * taxa / 100)
    if sit:
        return moeda(resp)
    else:
        return resp


# noinspection NonAsciiCharacters
def metade(preço, sit=False):
    """"→ Calcula a metade de um número."""
    resp = preço // 2
    if sit:
        return moeda(resp)
    else:
        return resp


# noinspection NonAsciiCharacters
def dobro(preço, sit=False):
    """"→ Calcula o dobro de um número."""
    resp = preço * 2
    if sit:
        return moeda(resp)
    else:
        return resp


def moeda(num):
    """"→ Retorna uma str formatada em forma monetária."""
    n = f'R${num:,.2f}'
    return n
