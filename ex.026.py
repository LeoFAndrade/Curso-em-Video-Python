import random

print('Vamos brincar de adivinhar números!')
numero = int(input('Digite um número de 0 à 5:'))
listanum = [0, 1, 2, 3, 4, 5]
PC = random.choice(listanum)
print(f'{PC}')
if numero == PC:
    print('Você acertou!')
else:
    print('Você errou!')
