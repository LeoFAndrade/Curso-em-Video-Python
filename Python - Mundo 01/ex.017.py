# Exerc�cio 017: Fa�a um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# tri�ngulo ret�ngulo, calcule e mostre o comprimento da hipotenusa.


import math
# Calculando a hipotenusa.
catetop = float(input(f'Comprimento do cateto oposto:'))
catetoad = float(input(f'Comprimento do cateto adjacente:'))
hipotenusa = math.hypot(catetop, catetoad)
print(f'A hipotenusa mede: {hipotenusa:.2f}')
