numero = int(input('Digite um número inteiro:'))
print('Escolha uma das bases de conversão:')
escolha = input('[ 1 ] Converter para BINÁRIO | [ 2 ] Converter para OCTAL | [ 3 ] Converter para HEXADECIMAL')
if escolha == '1':
    print(f'O seu número ficará assim: {bin(numero)}')
    end = ''
elif escolha == '2':
    print(f'O seu número ficará assim: {oct(numero)}')
    end = ''
elif escolha == '3':
    print(f'O seu número ficará assim: {hex(numero)}')
    end = ''
else:
    input('[ 1 ] Converter para BINÁRIO | [ 2 ] Converter para OCTAL | [ 3 ] Converter para HEXADECIMAL')
