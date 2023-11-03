# Exercício 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
print(f'O Nome é {aluno["Nome"]}\nA Média é {aluno["Média"]}')

if aluno['Média'] >= 7:
    print('Situação é igual a \033[1mAprovado')
elif aluno['Média'] <= 5 < 7:
    print('Situação é igual a \033[1mRecuperação')
else:
    print('Situação é igual a \033[1mReprovado')
