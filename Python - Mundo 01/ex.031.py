n1 = int(input('Digite um número:'))
n2 = int(input('Digite o segundo:'))
n3 = int(input('Digite o terceiro:'))
# Verificando o menor!
# Pra facilitar, deixei o menor como n1
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando agora o maior!
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor número é {menor}')
print(f'O maior número é {maior}')
