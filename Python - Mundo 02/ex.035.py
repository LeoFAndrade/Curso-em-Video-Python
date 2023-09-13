import enquiries
numero = int(input('Digite um número inteiro:'))
print('Escolha qual a conversão desejada:')
print('-1: para binário'), print('-2: para octal '), print('-3: para hexadecimal')
lista = ['1', '2', '3']
escolha = enquiries.choose('Digite a sua escolha', lista)
if escolha == 1:
    print(f'O seu número ficará assim: {bin(numero)}')
elif escolha == 2:
    print(f'O seu número ficará assim: {oct(numero)}')
elif escolha == 3:
    print(f'O seu número ficará assim: {hex(numero)}')
