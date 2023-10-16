# Exercício 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n = 0
numeros = tuple(int(input('Digite um número: ')) for x in range(0, 4))  # Usando da função range para repetição
print(numeros)
print(f'O número 9 apareceu: {numeros.count(9)} vezes')  # Função count

if 3 in numeros:  # Se em 'numeros' ter o número 3, o programa prossegue
    print(f'O valor 3 apareceu primeiro na posição: {numeros.index(3)+1}')
else:  # Caso contrário imprime uma mensagem
    print(f'O número 3 não apareceu nenhuma vez.')
print(f'Os números pares são: ', end='')

for n in numeros:
    if n % 2 == 0:
        print(f'{n}', end=' ')
