# Exercício 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

alunos = []  # Lista
num = 0  # Variável de controle

while True:
    nome = str(input('\033[1mDigite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota do aluno:'))  # Input do usuário
    nota2 = float(input('Digite a segunda nota do aluno:'))

    media = (nota1 + nota2)/2  # Calculando a média
    alunos.append([nome, nota1, nota2, media])  # Inserindo as informações na ficha do aluno
    
    resp = str(input('Deseja continuar ? [S/N]: ')).upper()
    if resp in "N":  # Pergunta ao usuário se deseja inserir mais fichas
        print('---' * 15)
        print(f'{"No.":<4}{"NOME":<8}{"MÉDIA":>8}')

        for index, itens in enumerate(alunos):  # Vai pegar os itens de cada índice de acordo com os parâmetros abaixo
            print(f'{index:<4}{itens[0]:<8}{itens[3]:>8.1f}')
            print('---' * 15)

        while True:  # Perguntará se o usuário deseja continuar a ver as notas de um aluno
            num = int(input('Deseja ver a nota de qual aluno ? [999 para parar]: '))
            if num == 999:
                print('FINALIZANDO')
                break
            if num <= len(alunos) - 1:
                print(f'Nome: {alunos[num][0]}\nNota1: {alunos[num][1]}\nNota2: {alunos[num][2]}')

# Consegui fazer boa parte sem ajuda, só tive que ver sobre a formatação do texto e um pouco sobre a parte de
# visualização de notas porque o programa de parada não estava funcionando por algum motivo. 02/11/2023
