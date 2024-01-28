# Exercício 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
# usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
# venceu ou perdeu.

import random
from time import sleep
print('\033[1;32m-=-' * 20)
print('\033[33mVamos brincar de adivinhar números!')
print('\033[1;32m-=-' * 20)
# O jogador começa escolhendo algum número de 0 a 5.
numero = int(input('\033[33mDigite um número de 0 à 5:'))
print('\033[0;32m-=-' * 20)
listanum = [0, 1, 2, 3, 4, 5]
PC = random.choice(listanum)
# Aqui o programa vai escolher aleatoriamente qualquer dos números listados acima.
print('\033[35mPROCESSANDO...')
sleep(3)
# O programa finaliza mostrando o resultado, e mostra uma mensagem diferente dependendo do resultado.
print(f'\033[33mPensei no número: {PC}')
if numero == PC:
    print('\033[1;32mPerdi, você acertou!')
else:
    print('\033[1;31mVocê errou, eu ganhei! kkkk')
print('\033[1;32 m-=-' * 20)
# Consegui fazer sem muita ajuda kkkkkk tô feliz demais kkkkkk Dia: 30/08/2023 h:18:00+-
