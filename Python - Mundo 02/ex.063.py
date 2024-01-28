# Exercício 063: Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de
# uma sequência de Fibonacci

s = '\033[31mSequência de Fibonacci\033[32m'
print(f'\033[32m{s:=^40}\033[m')

num = int(input('Digite quantos termos deseja exibir: '))  # Entrada do usuário
n = 0  # Primeiro termo
n2 = 1  # Segundo termo
cont = 2  # Variável de controle

print(f'{n} ➙', end=' ') # Início da sequência
while cont <= num:  # Enquanto a contagem for menor que "num" o programa vai repetir
    termo = n + n2  # Somando os termos, "primeiro" + "penúltimo"
    n2 = n  # O "penúltimo" termo se torna o "primeiro"
    n = termo  # E o "penúltimo" se torna o último, para o "último" se tornar o "primeiro" termo, resultado da soma
    cont += 1  # No final da repetição a contagem recebe + 1

    print(f'{termo} ➙', end=' ')  # Exibe os termos na tela de forma organizada
print('Fim')  # Quando a repetição acabar, finaliza com a mensagem Fim

