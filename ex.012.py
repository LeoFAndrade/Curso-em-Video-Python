salario = float(input('Digite o salário do funcionário:'))
aumento = float(input('Digite a porcentagem do aumento:'))
print(f'O aumento do salário é: {salario + (salario * aumento / 100):.2f}R$')
