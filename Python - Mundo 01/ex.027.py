# Exercício 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
# nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = input('Digite o seu nome:').title().split()
# Programa que exibe o nome e o último nome.
print(f'Bom te conhecer {nome[0]}!')
print(f'Seu primeiro nome é "{nome[0]}"')
print(f'E seu último nome é "{nome[-1]}"')
