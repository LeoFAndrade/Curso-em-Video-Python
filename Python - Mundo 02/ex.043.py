# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

x = '\033[35mJogo da velha\033[31m'
print(f'\033[31m{x :#^40}\033[m')
# Criando o jogo
player = int(input(f'\033[35mVamos jogar o {x}\033[m\n[ 0 ] Pedra \n[ 1 ] Papel \n[ 2 ] Tesoura '
                   f'\n\033[35mEscolha a sua opção:\033[m'))
# Criando as opções
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
# Exibindo os resultados do jogo
if pc == player:
    print(f'\033[33mA sua escolha foi a mesma que a minha: {itens[pc]}')
elif pc == 0 and player == 2 or pc == 1 and player == 0 or pc == 2 and player == 1:
    print(f'\033[31mVocê perdeu! a sua escolha: {itens[player]}, a minha escolha: {itens[pc]}')
else:
    print(f'\033[32mVocê ganhou! a sua escolha: {itens[player]}, a minha escolha: {itens[pc]} ')
