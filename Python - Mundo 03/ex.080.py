# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = list()
par = list()
impar = list()

while True:
    lista.append(int(input('Digite um número: ')))
    escolha = str(input('Deseja continuar ? (S/N) '))
    if escolha in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Os números digitados são: {lista}'
      f'\nOs pares são: {par}'
      f'\nE os ímpares: {impar}')
