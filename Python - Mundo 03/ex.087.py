# Exercício 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

alunos = []
flag = 999
num = 0
while True:
    nome = str(input('\033[1mDigite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota do aluno:'))
    nota2 = float(input('Digite a segunda nota do aluno:'))

    media = (nota1 + nota2)/2
    alunos.append([nome, nota1, nota2, media])
    
    resp = str(input('Deseja continuar ? [S/N]: ')).upper()
    if resp in "N":
        print('---' * 15)
        print(f'{"No.":<4}{"NOME":<8}{"MÉDIA":>8}')

        for index, itens in enumerate(alunos):
            print(f'{index:<4}{itens[0]:<8}{itens[3]:>8.1f}')
            print('---' * 15)

        while True:
            num = int(input('Deseja ver a nota de qual aluno ? [999 para parar]: '))
            if num == 999:
                print('FINALIZANDO')
                break
            if num <= len(alunos) - 1:
                print(f'Nome: {alunos[num][0]}\nNota1: {alunos[num][1]}\nNota2: {alunos[num][2]}')

# Consegui fazer boa parte sem ajuda, só tive que ver sobre a formatação do texto e um pouco sobre a parte de
# visualização de notas porque o programa de parada não estava funcionando por algum motivo. 02/11/2023
