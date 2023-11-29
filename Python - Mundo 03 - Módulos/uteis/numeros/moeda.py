def metade(numero):
    n = numero // 2
    return n


def aumentar(num, pc):
    num += num * pc / 100
    return num


def diminuir(num, pc):
    num -= num * pc / 100
    return num


def dobro(num):
    return num * 2


def moeda(num):
    num = f'R${num:,.2f}'
    return num
