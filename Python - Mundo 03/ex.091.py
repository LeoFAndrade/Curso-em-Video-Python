# Exercício 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o
# maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogos = {'Jogador1': randint(1, 6),  # Cada item do dicionário vai gerar um número entre 1 e 6
         'Jogador2': randint(1, 6),
         'Jogador3': randint(1, 6),
         'Jogador4': randint(1, 6)}

for index, valor in jogos.items():  # Vai exibir uma mensagem para cada índice e valor dentro do dicionário
    print(f'{index} tirou {valor} no dado')
    sleep(1)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)  # itemgetter ordena os dicionários, busca
# E retorna um item de um objeto. Ex:(lista, dicionário, tupla)
print('---' * 20)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: ficou para {v[0]} com {v[1]} pontos')
    sleep(1)
