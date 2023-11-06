# Exercício 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em
# dicionário, incluindo o total de gols feitos durante o campeonato.

dados = {}  # Dicionário
gols = []  # Lista

dados['Nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou ? '))  # Número de partidas do jogador

for x in range(partidas):  # O programa vai perguntar quantos gols o jogador fez em cada partida
    gols.append(int(input(f'Quantos gols no {x+1} jogo ? ')))  # Vai adicionar o valor em uma lista

print('-=-' * 20)
dados["gols"] = gols[:]  # Vai ser criado uma chave no dicionário aonde se vai armazenar a cópia da lista de gols
dados["Total"] = sum(gols)  # Aqui vai ser somado todos os gols da lista
print(dados)
print('-=-' * 20)

for i, v in dados.items():  # Aqui abaixo vai ser exibido cada índice e valor que há no dicionário
    print(f'O campo {i} tem o valor de {v}')
print('-=-' * 20)

print(f'O jogador {dados["Nome"]} jogou {len(dados["gols"])} partidas!\n')
for i, v in enumerate(dados["gols"]):  # O mesmo acima, porém com os dados da chave "gols"
    print(f' => Na partida {i+1}, fez {v} gols!')
