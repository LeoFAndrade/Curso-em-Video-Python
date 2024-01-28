# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer
# mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

num = int(input('Digite um número: '))  # Entrada do valor do primeiro termo usuário
razao = int(input('Digite a razão: '))  # Entrada do valor da razão do usuário
termo = int(input('Digite quantos termos da progressão exibir: '))  # Exibe a quantidade de termos de um P.A digitadas

cont = 0  # Variável de controle
tot = 0  # Variável de controle

while termo != 0:  # O programa vai repetir até "term" não se diferir de 0
    tot = tot + termo  # O Total vai basicamente receber o valor de 10

    while cont < tot:  # Enquanto o contador for menor que o total, o programa vai repetir
        num = num + razao  # Somando o número a razão para calcular o P.A
        cont += 1  # O Contador vai aumentar de acordo até atingir o total
        print(f'{num} ➙', end=' ')

    termo = int(input('Deseja continuar a P.A ?: '))  # O usuário tem a opção de continuar com a P.A se desejar
print('Fim')
