# Exercício 032: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Digite o ano:'))
if ano % 4 == 0:
    print(f'O ano "{ano}" é bissexto!!!')
else:
    print(f'O ano "{ano}" não é bissexto!!!')
