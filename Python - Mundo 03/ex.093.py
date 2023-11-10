# Exercício 095: Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador.

jogadores = list()
jogador = {}
jogador['Index'] = 0

while True:

    jogador['Nome'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou ? '))
    gols = []

    for p in range(partidas):
        gol = int(input(f'Digite quantos gols o {jogador["Nome"]} fez na partida {p}: '))
        gols.append(gol)

    while True:
        r = str(input('Deseja continuar ? [S/N] '))
        if r in 'SsNn':
            jogador['Gols'] = gols
            jogador['Total'] = sum(gols)
            jogadores.append(jogador.copy())
            jogador['Index'] += 1
            break
        print('Por favor apenas digite S ou N: ')
    if r in 'Nn':
        break

print("\033[1m-=-" * 20)
print(jogadores)
print("---" * 20)

print(f'{"No.":<4}{"NOME":<8}{"GOLS":>8}{"TOTAL":>15}')

for jogador in jogadores:
    for valor in jogador.values():
        print(f'{jogador["Index"]!s:<4}{jogador["Nome"]!s:<8}{jogador["Gols"]!s:>8}{jogador["Total"]!s:>15}')
        break
print("---" * 20)
while True:
    busca = int(input('Deseja ver os dados de qual jogador ? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'Não existe jogador com o código {busca}')
    else:
        print(f'Levantamento do Jogador {jogadores[busca]["Nome"]}')
    for part, gol in enumerate(jogadores[busca]['Gols']):
        print(f'    No jogo {part+1} fez {gol}.')
