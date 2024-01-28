# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o
# recurso de mostrar que tipo de triângulo será formado:
print('\033[32m-=-' * 20), print('Analisador de triângulo 2.0'), print('-=-' * 20, '\033[m')
azul = '\033[34m'
x = '\033[m'

r1 = int(input(f'Primeiro {azul}segmento{x}:'))
r2 = int(input(f'Segundo {azul}segmento{x}:'))
r3 = int(input(f'Terceiro {azul}segmento{x}:'))
# Analisaremos se as três retas podem formar um triângulo ou não.
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo')
    # Será analisado se pode ser um triângulo Equilátero
    if r1 == r2 == r3:
        print('Os segmentos formam um \033[33mEQUILÁTERO!')
        if r1 != r2 != r3 != r1:
            # Aqui será o Escaleno
            print('Os segmentos formam um \033[33mESCALENO')
            # E Aqui, simplificando é Isósceles
else:
    print('Os segmentos formam um \033[33mISÓSCELES')
