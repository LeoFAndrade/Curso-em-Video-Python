# Exercício 084: Faça um programa que leia nome e peso de vários pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantos pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = dados = []
maior = menor = 0
count = 0
pesomaior = pesomenor = ''
while True:
    dados.append(input('Digite o nome da pessoa: '))
    dados.append(int(input('Digite o peso da pessoa: ')))
    lista.append(dados[:])

    for x in lista:

        if len(dados) == 0:
            maior = menor = dados[1]
        else:
            if dados[1] >= maior:
                maior = dados[1]
                pesomaior = dados[0]
            if dados[1] <= maior:
                menor = dados[1]
                pesomenor = dados[0]
        dados.clear()
    resp = input('Deseja continuar ? [S/N]: ').upper()
    count += 1
    if resp in 'N':
        break
print(f'O total de pessoas cadastradas foram: {count}')
print(f'O maior peso registrado foi de: {maior}KG')
print(f'A pessoa de maior peso é: {pesomaior}')
print(f'O menor peso registrado foi de: {menor}KG')
print(f'A pessoa de menor peso é: {pesomenor}')
