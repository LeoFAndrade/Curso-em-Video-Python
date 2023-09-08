km = float(input('Qual é a distância da viagem ?'))
# Calcula o preço de uma viagem, se for superior à 200Km, a cobrança será de 0.45R$ ao invés de 0.50R$.
if km <= 200.00:
    print(f'A Sua viagem ficou: R${km * 0.50}')
else:
    print(f'A Sua viagem ficou: R${km * 0.45}')
