velocidade = float(input('Qual a velocidade atual do carro:'))
# O programa verifica se a velocidade é superior à 80Km, se for a multa é de 7.00R$ por cada km acima do limite.
if velocidade > 80.00:
    multa = (velocidade - 80.00) * 7
    print('Você ultrapassou o limite de velocidade permitido de 80Km/h!')
    print(f'Você deve pagar uma multa de {multa}R$')
else:
    print('Tenha um bom dia, dirija com segurança')
print('Dirija com cuidado tenha um bom dia')
