# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

x = 'Fatorial'
print(f'{x:=^40}')

num = int(input('Digite um número: '))
count = 1  # Serve como um operando
resultado = 1  # A mesma coisa acima, com a diferença de que serve como resultado simultaneamente

while count <= num:  # Se o contador não for menor ou igual que o número, repita

    resultado *= count  # O resultado vai se multiplicar com o count e após isso, se tornará o novo valor calculado
    # Exemplo: resultado * count = X, X = resultado. O programa vai se repetir até a condição em while ser satisfeita

    count += 1  # No final do laço o contador vai adicionar mais 1 na sua contagem
    print(f'O resultado da fatoração é: {resultado} ')
