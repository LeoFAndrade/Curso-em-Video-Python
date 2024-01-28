# Exercício Python 038: Escreva um programa que leia dois números inteiros e
# compare-os. Mostrando uma mensagem na tela:

num1 = int(input('Digite um número:'))
num2 = int(input('Digite o segundo número:'))
if num1 > num2:
    print('O maior número é o primeiro!!!')
elif num2 > num1:
    print('O maior número é o segundo!!!')
elif num1 == num2:
    print('Ambos os valores são iguais!!!')
