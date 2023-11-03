# Exercício 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
print(f'O Nome é {"Nome"}\nA Média é {"Média"}')
if aluno['Média'] >= 7:
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')
