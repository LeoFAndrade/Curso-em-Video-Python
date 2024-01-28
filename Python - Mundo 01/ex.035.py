# Exercício 035: Desenvolva um programa que leia o comprimento de três vetores e diga ao usuário se elas podem ou não
# formar um triângulo.

r1 = int(input('Digite o tamanho da primeira reta:'))
r2 = int(input('Digite o tamanho da segunda:'))
r3 = int(input('Digite o tamanho da última reta:'))
# Analisaremos se as três retas podem formar um triângulo ou não.
maior = r1
if r2 and r3 > r1:
    maior = r2
if r3 and r2 > r1:
    maior = r3
if r1 and r3 > r2:
    print('É possível formar um triângulo com estas retas')
else:
    print('Não é possível formar um triângulo com estas retas')
