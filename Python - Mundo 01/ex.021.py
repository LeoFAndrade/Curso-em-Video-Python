numero = int(input('Digite um número qualquer:'))
u = numero//1 % 10
d = numero//10 % 10
c = numero//100 % 10
m = numero//1000 % 10
print(f'A unidade do número é: {u}')
print(f'A dezena do número é: {d}')
print(f'A centena do número é: {c}')
print(f'A milhar do número é: {m}')
