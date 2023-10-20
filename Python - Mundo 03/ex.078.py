# Exercício 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na
# posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

numeros = []

for c in range(5):

    num = int(input('Digite um número: '))
    if c == 0 or num > numeros[-1]:  # Se o número digitado for maior que o primeiro, será adicionado na última
        # posição da lista
        numeros.append(num)

    else:
        pos = 0  # Posição 0
        while pos < len(numeros):
            if num <= numeros[pos]:  # Se o número for menor ou igual à posição, ele será adicionado à posição
                numeros.insert(pos, num)  # Adicionando na posição específica
                break
            pos += 1  # Avança +1 a posição
print(f'Os números ordenados ficam na posição {numeros}')
