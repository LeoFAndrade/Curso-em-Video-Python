# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# Usando a estrutura while

num = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
cont = 0
while cont < 10:
    num = num + razao
    cont += 1
    print(f'{num} ➙', end=' ')
print('Fim')
