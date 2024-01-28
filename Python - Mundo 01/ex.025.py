# Exercício 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o seu nome:').strip())
# O Programa basicamente analisa se tem "Silva" em um nome.
print(f'Tem Silva no seu nome ? {"Silva".lower() in nome}')
