# Exercício 086: Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]

while True:
    for n in range(0, 3):
        numero = int(input(f'Digite um valor para a posição [0:{n}]: '))
        matriz[0].append(numero)

    for n in range(0, 3):
        numero = int(input(f'Digite um valor para a posição [1:{n}]: '))
        matriz[1].append(numero)

    for n in range(0, 3):
        numero = int(input(f'Digite um valor para a posição [2:{n}]: '))
        matriz[2].append(numero)
    break

print(f'\033[1m[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]\n'
      f'[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]\n'
      f'[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2] } ]')
