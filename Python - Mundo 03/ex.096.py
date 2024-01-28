# Exercício 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

# noinspection NonAsciiCharacters
def área(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}')


print('\033[1mCONTROLE DE TERRENOS')
print('---' * 10)

larg = float(input('LARGURA (m): '))
compr = float(input('COMPRIMENTO (m): '))
área(larg, compr)
