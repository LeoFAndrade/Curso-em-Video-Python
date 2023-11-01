# Exercício 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos
# jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
from time import sleep


print('===' * 15)
print(f'\033[1m{"JOGO DA MEGASENA":^45}')
print('===' * 15)

while True:  # O programa vai rodar até terminar todas as condições
    jogada = int(input('Quantos jogos você deseja sortear ? '))  # Input do usuário

    for jog in range(0, jogada):  # O programa vai repetir quantas vezes o usuário desejou
        dados = (random.sample(range(0, 61), 6))  # Sample vai pegar algum número randomicamente de
        # range entre 0 e 61 e depois adicionar a lista de dados
        sleep(0.5)  # Pequeno intervalo de tempo
        print(sorted(dados))  # Retorna a lista de forma separada uma da outra
    break
