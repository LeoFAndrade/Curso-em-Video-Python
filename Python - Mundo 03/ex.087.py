# Exercício 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somacol = maiorval = 0

while True:
    for linha in range(0, 3):
        for coluna in range(0, 3):
            matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}:{coluna}]: '))
            if matriz[linha][coluna] % 2 == 0:
                soma += matriz[linha][coluna]

            if matriz[linha][2]:
                somacol += matriz[linha][2]

            if coluna == 0:
                maiorval = matriz[1][coluna]
            if matriz[1][coluna] > maiorval:
                maiorval = matriz[1][coluna]
    break
print(f'\033[1m[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]\n'
      f'[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]\n'
      f'[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')
print(f'A soma de todos os pares digitados é: {soma}')
print(f'A soma dos valores da terceira coluna é: {somacol}')
print(f'O maior valor da segunda linha é: {maiorval}')
