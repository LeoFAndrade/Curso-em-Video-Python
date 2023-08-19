dia = int(input('Por quantos dias o carro foi alugado ?'))
km = float(input('Quantos Km foram rodados ?'))
pago = (dia * 60) + (km * 0.15)
print(f'O total à ser pago é de {pago:.2f}')