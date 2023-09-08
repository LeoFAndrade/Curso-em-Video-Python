import random
from time import sleep
print('Vamos brincar de adivinhar números!')
# O jogador começa escolhendo algum número de 0 a 5.
numero = int(input('Digite um número de 0 à 5:'))
listanum = [0, 1, 2, 3, 4, 5]
PC = random.choice(listanum)
# Aqui o programa vai escolher aleatoriamente qualquer dos números listados acima.
print('PROCESSANDO...')
sleep(3)
# O programa finaliza mostrando o resultado, e mostra uma mensagem diferente dependendo do resultado.
print(f'{PC}')
if numero == PC:
    print('Droga, você acertou!')
else:
    print('Você errou, eu ganhei! kkkk')
# Consegui fazer sem muita ajuda kkkkkk tô feliz demais kkkkkk Dia: 30/08/2023 h:18:00+-
