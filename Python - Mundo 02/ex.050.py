# Exercício Python 052: Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
if num % 2 != 0 or num == 2:  # Se o resultado não for de 0, então não é número primo
    print(f'O número {num} É primo.')
else:
    print(f'O número {num} Não é primo')
