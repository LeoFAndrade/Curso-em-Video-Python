# Exercício 084: Faça um programa que leia nome e peso de vários pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantos pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = []
dados = []
maior = menor = count = 0

while True:
    dados.append(input('Digite o nome da pessoa: '))
    dados.append(int(input('Digite o peso da pessoa: ')))
    lista.append(dados[:])

    for x in lista:

        if len(dados) == 0:
            maior = menor = dados[1]
        else:
            if dados[1] > maior:
                maior = dados[1]
            if dados[1] < maior:
                menor = dados[1]
    dados.clear()
    resp = input('Deseja continuar ? [S/N]: ').upper()
    count += 1

    dados.clear()

    if resp in 'N':
        break
print(f'O total de pessoas cadastradas foram: {count}')
print(f'As pessoas de maior peso são: {maior}')
print(f'As pessoas de menor peso são: {menor}')
