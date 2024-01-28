# Exercício 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de
# um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog='', gol=0):
    print(f'O Jogador {jog} fez {gol} gol(s) no campeonato!')


# Programa Principal
nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Números de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    nome = '<desconhecido>'

ficha(nome, gols)
