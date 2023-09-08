import math
# Calculando a hipotenusa.
catetop = float(input(f'Comprimento do cateto oposto:'))
catetoad = float(input(f'Comprimento do cateto adjacente:'))
hipotenusa = math.hypot(catetop, catetoad)
print(f'A hipotenusa mede: {hipotenusa:.2f}')
