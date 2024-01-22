def leiaDinheiro(msg):
    while True:
        valor = input(msg).replace(',', '.')
        if valor.replace('.', '', 1).isdigit():
            return float(valor)
        else:
            print('\033[1;31mValor inválido. Digite um valor monetário válido.\033[m')


def leiaInt(número):
    while True:
        try:
            print(número, end='')
            número = int(input())
            return número

        except ValueError:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
