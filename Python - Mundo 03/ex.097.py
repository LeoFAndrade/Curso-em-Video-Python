# Exercício 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
# inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

print('-=-' * 15)


def maior(*valores):
    print('Analisando os valores passados...')
    numero = valores
    for numero in valores:
        sleep(0.5)
        print(numero, end=' ')
    print(f'Foram informados {len(valores)} valores ao todo.\nO maior valor informado foi {max(valores)}')
    print('-=-' * 15)


maior(0, 4, 3, 2, 1)
maior(1, 4, 6, 9, 10)
maior(0)
