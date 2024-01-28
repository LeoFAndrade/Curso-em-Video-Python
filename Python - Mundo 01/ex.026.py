# Exercício 026: Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

fr = input('Digite uma frase:').lower().strip()
# Uma aplicação simples para analisar certas características sobre uma frase.
frase = fr.count('a')
letraA1 = fr.index('a')
letraA2 = fr.rindex('a')
print(f'A letra "A" aparece {frase} na frase')
print(f'A primeira letra "A" apareceu primeiro na posição {letraA1}')
print(f'E a ultima letra "A" aparece na posição {letraA2}')
