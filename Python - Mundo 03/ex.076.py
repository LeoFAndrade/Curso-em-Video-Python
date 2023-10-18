# Exercício 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e menor valor digitados e a s suas respectivas posições na lista.

valores = []  # Lista
posmaior = posmenor = 0  # Variáveis

for count in range(0, 5):  # Repetindo a pergunta 5 vezes
    valores.append(int(input('Digite um número: ')))  # Os valores digitados vão ser anexados a lista

posmaior = valores.index(max(valores))  # Pegando o maior valor da lista e encontrando a sua posição específica
posmenor = valores.index(min(valores))  # E agora a posição do menor

print(f'O maior valor é: \033[1;32m{max(valores)}\033[m na posição: \033[1;35m{posmaior+1}\033[m da lista'
      f'\nO menor valor é: \033[1;31m{min(valores)}\033[m na posição: \033[1;35m{posmenor+1}\033[m da lista')
