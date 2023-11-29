
def aumentar(num, pc, sit=False):
    num += num * pc / 100
    if sit:
        return moeda(num)
    else:
        return num


def diminuir(num, pc, sit=False):
    num -= num * pc / 100
    if sit:
        return moeda(num)
    else:
        return num


def metade(numero, sit=False):
    num = numero // 2
    if sit:
        return moeda(num)
    else:
        return num


def dobro(num, sit=False):
    if sit:
        return moeda(num)
    else:
        return num


def moeda(num):
    n = f'R${num:,.2f}'
    return n
