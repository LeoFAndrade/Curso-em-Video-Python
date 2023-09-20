# Exercício Python 046: Faça um programa que mostre
# uma contagem regressiva na tela para o estouro de fogos de artifício, indo de 10 até 0, com
# uma pausa de 1 segundo entre eles.

from time import sleep

print('\033[31mContagem regressiva para os fogos!!!!\033[33m')
# Usando for para iterar e range para a inversão da contagem
for x in range(10, 0, -1):
    # Usando de sleep para a contagem regressiva
    sleep(1)
    print(x)
print('\033[31mBUM BUM POW')
