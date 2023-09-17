# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre sua classificação,
# conforme a tabela abaixo:

print('\033[32m-=-' * 20), print('\033[33mCalculador de IMC\033[m'), print('\033[32m-=-' * 20, '\033[m')
# Calculando o IMC usando o método usado para o cálculo
altura = float(input('Digite a altura: (m)'))
peso = float(input('Digite o peso: (Kg)'))
imc = peso / (altura ** 2)
# Formatando para melhor visualização
print(f'{imc:.1f}')
# O programa vai classificar conforme o peso calculado anteriormente
if imc <= 18.5:
    print(f'\033[31mAbaixo do peso: {imc:.1f}')
elif 18.5 <= imc <= 25:
    print(f'\033[32mPeso ideal: {imc:.1f}')
elif 25 <= imc <= 30:
    print(f'\033[33mSobrepeso: {imc:.1f}')
elif 30 <= imc <= 40:
    print(f'\033[33mObesidade: {imc:.1f}')
elif imc > 40:
    print(f'\033[31mObesidade mórbida: {imc:.1f}')
