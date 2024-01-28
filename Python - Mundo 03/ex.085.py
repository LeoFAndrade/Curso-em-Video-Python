# Exercício 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]

for x in range(0, 7):
    num = int(input('Digite um número: '))

    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f'Números pares: {lista[0]}')
print(f'Números ímpares: {lista[1]}')
lista = sum(lista, [])
lista.sort()
print(f'Os números em ordem crescente: {lista}')
