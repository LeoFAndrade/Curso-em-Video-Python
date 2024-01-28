# Exercício 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o valor do salário:'))
# Verificando se o tamanho do salário é superior à 1.250R$ e calculando seu aumento de 10%
if salario > 1.250:
    salario = salario + (salario*10)/100
    print(f'O aumento ficou no total: R${salario:.0f}')
# Verificando se o tamanho do salário é igual ou menor à 1.250, acrescentando o aumento de 15%
if salario <= 1.250:
    salario = salario + (salario*15)/100
    print(f'O aumento ficou no total: R${salario:.0f}')
