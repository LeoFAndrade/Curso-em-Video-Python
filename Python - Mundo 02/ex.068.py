# Exercício 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato

cont = conta = mil = menor = 0  # Variáveis de controle
barato = ''

while True:
    print('===' * 15)
    produto = str(input('Digite o nome do produto: ')).upper()
    # noinspection NonAsciiCharacters
    preço = float(input('Digite o preço: R$: '))
    cont += 1
    conta += preço

    if preço > 1000:
        mil += 1

    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar ? [S/N] ').upper()
        print('===' * 15)
    if resp == 'N':
        break

print(f'O total gasto na compra foi de {conta:.2f}')
print(f'Há {mil} produtos acima de R$:1000.00!')
print(f'O produto mais barato é {barato} custa: R$: {menor:.2f}')
