salario = float(input('Digite o valor do salário:'))
# Verificando se o tamanho do salário é superior à 1.250R$ e calculando seu aumento de 10%
if salario > 1.250:
    salario = salario + (salario*10)/100
    print(f'O aumento ficou no total: {salario:.0f}R$')
# Verificando se o tamanho do salário é igual ou menor à 1.250, acrescentando o aumento de 15%
if salario <= 1.250:
    salario = salario + (salario*15)/100
    print(f'O aumento ficou no total: {salario:.0f}R$')
