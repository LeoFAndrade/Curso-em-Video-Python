# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

cor = '\033[31mpeso\033[m'
maior = 0
menor = 0
for x in range(1, 6):
    peso = float(input(f'Digite o {cor} da {x}ª pessoa: '))
    if x == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso lido é {maior}ª')
print(f'O menor peso lido é {menor}ª')
