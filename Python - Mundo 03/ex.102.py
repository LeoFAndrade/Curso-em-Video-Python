# Exercício 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input()
# do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n')

# noinspection NonAsciiCharacters
def leiaInt(número):
    while True:
        try:
            print(número, end='')
            número = int(input())
            return número

        except ValueError:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')


# Programa Principal
num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}!')
