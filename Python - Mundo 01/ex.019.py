from random import shuffle
# O programa organiza aleatoriamente os nomes em uma lista.
nome1 = input('Primeiro aluno:')
nome2 = input('Segundo aluno:')
nome3 = input('Terceiro aluno:')
nome4 = input('Quarto nome:')
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print(f'A ordem de alunos é:{lista}')
