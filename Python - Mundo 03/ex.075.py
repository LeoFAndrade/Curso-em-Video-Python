# Exercício 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve
# mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Toyota', 'Mitsubishi', 'Honda', 'Suzuki', 'Subaru', 'Hyundai', 'Mercedes', 'BMW', 'Porsche', 'Volkswagen',
            'Fiat', 'Peugeot')
vogal = 'AaEeIiOoUu'

for palavra in palavras:
    print(f'\n{palavra} -', end=' ')
    for letra in palavra:
        if letra in vogal:
            print(letra, end=' ')
