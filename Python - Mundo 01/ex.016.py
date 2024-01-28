# Exercício 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math
# Truncando o valor decimal.
numero = float(input('Digite um número decimal qualquer:'))
truncado = math.trunc(numero)
print(f'A porção inteira do número digitado {numero} é {truncado}')
