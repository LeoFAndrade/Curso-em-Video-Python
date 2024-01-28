# Exercício 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
# ele, tendo o nome deles e escrevendo o nome do escolhido.

import random
# O programa vai escolher randomicamente o aluno.
nome1 = input('Primeiro aluno:')
nome2 = input('Segundo aluno:')
nome3 = input('Terceiro aluno:')
nome4 = input('Quarto nome:')
lista = [nome1, nome2, nome3, nome4]
print(f'O aluno escolhido foi:{random.choice(lista)}')
