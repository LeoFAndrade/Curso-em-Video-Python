# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:  # Aqui presume a condição será cumprida, se não for ela vai se repetir
    sexo = str(input('Digite o seu sexo (M/F): ')).strip().upper()  # O usuário deve digitar uma das opções
    if sexo == 'M' or sexo == 'F':  # Aqui será analisado se cumpre uma das duas das condições acima
        print(f'O digitado foi {sexo}')
        break
