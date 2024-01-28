# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

num = int(input('Digite o número: '))  # Pegando os valores respectivamente do usuário
razao = int(input('Digite a razão: '))
ultimo = num + (10 - 1) * razao   # Somando os termos
for x in range(num, ultimo + razao, razao):  # Organizando a ordem aritmética
    print(f'{x} ➙', end=' ')
print('Fim')
