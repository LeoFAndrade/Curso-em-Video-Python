km = float(input('Qual é a distância da viagem ?'))
if km <= 200.00:
    print(f'A Sua viagem ficou: {km * 0.50}R$')
else:
    print(f'A Sua viagem ficou: {km * 0.45}R$')
