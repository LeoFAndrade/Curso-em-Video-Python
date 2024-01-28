# Exercício 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogador só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou
# no final do jogo

from random import randint

PC = randint(0, 11)  # O PC vai escolher algum número aleatório entre 0 e 10

print('\033[1;35m-=-' * 20)
print('\033[1;33mVamos jogar Par ou Ímpar!')
print('\033[1;35m-=-\033[33m' * 20)

while True:
    player = int(input('\033[1;33mDigite um valor: '))   # Entrada do jogador
    player2 = str(input('Você quer ímpar ou par ? [I/P]')).upper()[0]
    soma = player + PC  # Soma dos valores do jogador e PC
    print(f'{player} + {PC} = {soma}\033[m')

    if player2 == 'P':  # Se o jogador escolher 'Par' as seguintes situações se apresentam abaixo
        if soma % 2 == 0:  # Se a soma dividido por 2 dar '0', então o resultado é par.
            print(f'\033[32mA soma total dá {soma}, portanto é Par.\nVOCÊ GANHOU\033[m')
        else:  # Caso contrário, não é
            print(f'\033[31mA soma total dá {soma}, portanto é Ímpar.\nVOCÊ PERDEU\033[m')
            break
    elif player2 == 'I':  # O jogador pode escolher 'Ímpar'
        if soma % 2 != 0:  # Se o resultado diferir de '0' então é ímpar
            print(f'\033[32mA soma total dá {soma}, portanto é Ímpar.\nVOCÊ GANHOU\033[m')
        else:  # Caso contrário, então é par
            print(f'\033[31mA soma total dá {soma}, portanto é Par.\nVOCÊ PERDEU\033[m')
            break
