# Exercício Python 037: Escreva um programa em Python que leia um número inteiro
# qualquer e peça para o usuário escolher qual será a base de conversão: 1 para
# binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases de conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
escolha = int(input('Digite a sua escolha:'))
# O programa vai converter o número segundo a escolha.
if escolha == 1:
    print(f"O seu número ficará assim: {bin(numero).replace('0b','')}")
    end = ''
elif escolha == 2:
    print(f'O seu número ficará assim: {oct(numero).replace("0o", "")}')
    end = ''
elif escolha == 3:
    print(f'O seu número ficará assim: {hex(numero).replace("0x", "")}')
    end = ''
else:
    print('Opção inválida')
