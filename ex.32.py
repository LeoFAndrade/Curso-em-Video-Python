salario = float(input('Digite o valor do salário:'))
if salario > 1.250:
    salario = salario + (salario*10)/100
    print(f'O aumento ficou no total: {salario:.0f}R$')
if salario <= 1.250:
    salario = salario + (salario*15)/100
    print(f'O aumento ficou no total: {salario:.0f}R$')
