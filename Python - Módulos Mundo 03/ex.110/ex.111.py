# Exercício 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
# de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() coma a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            número = int(input(msg))
            print(f'Você acabou de digitar o número {número}!')

        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;33mEntrada de valor interrompida pelo usuário!')

        else:
            return número


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
            print(f'Você acabou de digitar o número {num}!')

        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')

        except KeyboardInterrupt:
            print('\033[1;33mO usuário interrompeu o programa!\033[m')
            return 0
        else:
            return num


a = leiaInt('Digite um número inteiro: ')
print(a)
b = leiaFloat('Digite um número real: ')
print(b)
