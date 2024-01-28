# Exercício 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário do funcionário:'))
aumento = float(input('Digite a porcentagem do aumento:'))
# Verificando o salário após o aumento.
print(f'O aumento do salário é: {salario + (salario * aumento / 100):.2f}R$')
