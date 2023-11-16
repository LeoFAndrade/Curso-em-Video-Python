# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores PARES sorteados pela função anterior.

from random import randint
from time import sleep
numeros = list()


def sorteia(lista):
    for contador in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('FIM')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando todos os valores pares da lista {lista}, resulta em: {soma} ', end='')


sorteia(numeros)
somapar(numeros)
