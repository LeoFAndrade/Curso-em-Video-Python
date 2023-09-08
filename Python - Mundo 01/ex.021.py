numero = int(input('Digite um número qualquer:'))
# O programa vai calcular respectivamente cada unidade de medida.
unidade = numero//1 % 10
dezena = numero//10 % 10
centena = numero//100 % 10
milhar = numero//1000 % 10
print(f'A unidade do número é: {unidade}')
print(f'A dezena do número é: {dezena}')
print(f'A centena do número é: {centena}')
print(f'A milhar do número é: {milhar}')
