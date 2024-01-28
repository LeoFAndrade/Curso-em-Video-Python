# Exercício 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Digite o nome da cidade:').strip().lower()
print(cidade.startswith("santo"))
