# Exercício Python 058:
# Melhore o jogo do Desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import choice

c = 0  # Contador de jogadas
listanum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Essa lista será usada para a adivinhação
PC = choice(listanum)  # O computador vai escolher aleatoriamente dentro da lista

print('\033[35m-=-' * 20)
print('\033[36mVamos brincar de adivinhar números!')
print('\033[35m-=-\033[36m' * 20)

while True:  # Presumindo VERDADE o PC vai repetir até as condições serem atendidas
    player = int(input('\033[36mDigite um número de 0 a 10: '))  # O jogador faz a sua jogada
    c += 1  # Cada vez que o jogador fizer a sua jogada, o contador aumenta

    if player < PC:  # Se a jogada for menor que a do PC, o jogador será orientado a jogar menor
        print('\033[31mMais...')
    elif player > PC:  # Se for maior, o jogador é orientado a jogar menor
        print('\033[32mMenos...')
    print('\033[35m-=-' * 20)
    if player == PC:  # Se o jogador acertou, o programa finaliza com a contagem de quantas vezes tentadas
        print(f'Você acertou ! Você precisou de {c} vezes para acertar')
        break
