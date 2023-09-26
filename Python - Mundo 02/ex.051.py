# Exercício Python 053: Crie um programa que leia uma frase qualquer e
# diga se ela é um palíndromo, desconsiderando os espaços.

pali = str(input('Digite algo: ')).strip().upper().replace(' ', '')
if pali == pali[::-1]:  # Aqui reverterá a frase para analisar se é igual ou não
    print(f'A palavra {pali} é palíndromo')
else:
    print(f'A palavra {pali} não é palíndromo')
print(f'A palavra ao contrário fica assim: {pali[::-1]}')
