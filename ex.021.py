numero = int(input('Digite um número qualquer:'))
divisao = [int(n) for n in str(numero)]
print(f'A unidade do número é: {divisao[-1]}')
print(f'A dezena do número  é: {divisao[-2]}')
print(f'A centena do número é: {divisao[-3]}')
print(f'A milhar do número  é: {divisao[-4]}')
