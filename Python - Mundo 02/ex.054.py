# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

atual = datetime.date.today().year  # Pegando a data atual
tot = 0
tot2 = 0
for x in range(1, 8):  # Repetindo a mesma pergunta 7 vezes
    data = int(input(f'Digite o ano de nascimento da {x}ª: '))
    idade = atual - data  # Calculando a idade
    if idade >= 21:  # Se for 21 ou maior de 21 é maior de idade
        tot += 1  # Para cada maior de idade é +1 para a quantidade total
    else:
        tot2 += 1  # E aqui é a quantidade total de menores de idade
print(f'Temos no total {tot} de maiores de idade')
print(f'E {tot2} menores de idade!')
