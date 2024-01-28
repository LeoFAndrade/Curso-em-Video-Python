# Exercício 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)

print('Os números sorteados são: ', end='')
while numeros in range(0, 5):
    numeros = randint(0, 11)

print(numeros, end=' ')
print(f'\nO maior valor é: {max(numeros)}')
print(f'O menor número é: {min(numeros)}')
