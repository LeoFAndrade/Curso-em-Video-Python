# Exercício 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já existe lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []

while True:
    num = int(input('Digite um número: '))
    if num not in numeros:  # Se o número digitado não estiver na lista, ele será adicionado
        numeros.append(num)
    else:
        print('Valor duplicado! Digite outro!')  # Se for duplicado, o programa vai pedir se deseja continuar

    resp = str(input('Deseja continuar ? [S/N]: ')).upper()
    if resp in 'SN':
        if resp == 'N':
            break
numeros.sort(reverse=True)
print(f'Os números digitados são: {numeros}')
