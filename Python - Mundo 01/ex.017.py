import math
angulo = float(input('Digite o ângulo:'))
# Calculando seno, cosseno e tangente respectivamente.
SENO = math.sin(math.radians(angulo))
print(f'O Ângulo de {angulo} tem o SENO de {SENO:.2f}')
COSSENO = math.cos(math.radians(angulo))
print(f'O COSSENO de {angulo} tem é de {COSSENO:.2f}')
TANGENTE = math.tan(math.radians(angulo))
print(f'E a TANGENTE de {angulo} é {TANGENTE:.2f}')
