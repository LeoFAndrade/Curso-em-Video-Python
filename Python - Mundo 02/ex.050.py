# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre
# a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for x in range(0, 6):  # Aqui o programa vai perguntar a mesma coisa 6 vezes
    numero = int(input('Digite um número: '))  # O usuário vai digitar os números
    if numero % 2 == 0:
        soma += numero
print(f'A soma dos números pares resulta: {soma}')
