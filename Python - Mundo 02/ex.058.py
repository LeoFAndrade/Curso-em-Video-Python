# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

x = 'Fatorial'
print(f'{x:=^40}')

num = int(input('Digite um número: '))
count = 1  # Serve como um contador que aumentará conforme 
resultado = 1

while count <= num:  # Se o contador não for menor ou igual que o número, repita

    resultado *= count  # O resultado vai se multiplicar com o count e após isso, se tornará o novo valor calculado
    # Exemplo: resultado * count = X, X = resultado. O programa vai se repetir até while ser satisfeito

    count += 1  # No final do laço o contador vai adicionar mais 1 na sua contagem
    print(f'O resultado da fatoração é: {resultado} ')
