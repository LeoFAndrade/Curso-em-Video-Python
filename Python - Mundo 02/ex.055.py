# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

cor = '\033[31mpeso\033[m'
maior = 0
menor = 0
for x in range(1, 6):
    peso = float(input(f'Digite o {cor} da {x}ª pessoa: '))
    if x == 1:  # Aqui começara pela primeira pessoa, considerando ela simultaneamente a de maior e menor peso
        maior = peso
        menor = peso
    elif peso > maior:  # Se outro valor for maior que o primeiro valor, então passa a ser considera o de maior peso
        maior = peso
    elif peso < menor:  # A mesma coisa acima, porém neste caso com o menor peso
        menor = peso
print(f'O maior peso lido é {maior}ª')
print(f'O menor peso lido é {menor}ª')
