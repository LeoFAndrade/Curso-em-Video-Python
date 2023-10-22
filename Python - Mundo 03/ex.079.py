# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista

lista = []
c = 0
while True:
    num = lista.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar ? [S/N]: ')).upper()
    lista.sort(reverse=True)
    c += 1
    if resp in 'SN':
        if resp == 'N':
            print(f'Foram digitados {c} números!'
                  f'\nA lista em ordem decrescente fica {lista}')
            if 5 in lista:
                print('O valor "5" foi encontrado na lista ')
            else:
                print('O valor "5" não foi encontrado na lista')
                break
