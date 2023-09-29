# Exercício Python 059: Crie um programa que leia dois valores e
# mostre um menu na tela:
# [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] numero ao quadrado [ 6 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

num1 = float(input('\033[35mDigite um número: '))
num2 = float(input('\033[35mDigite um número: '))

while True:
    print('\033[32m [ 1 ] somar\n [ 2 ] multiplicar\n [ 3 ] maior\n [ 4 ] novos números\n [ 5 ] numero ao quadrado \n '
          '[ 6 ] sair do programa')
    choice = int(input('\033[35mDigite a sua escolha: '))

    if choice == 1:
        soma = num1 + num2

        print(f'A soma dos dois números é: \033[31m{soma} ')

    elif choice == 2:
        mult = num1 * num2

        print(f'A multiplicação de ambos os números é: \033[31m{mult}')

    elif choice == 3:
        if num1 > num2:
            print(f'Maior numero: \033[31m{num1}')
        else:
            print(f'Maior numero: \033[31m{num2}')

    elif choice == 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite um número: '))

    elif choice == 5:
        num0 = int(input('Qual número deseja elevar ao quadrado: '))
        if num0 == num1:
            pot = num0 * num0

            print(f'A potenciação de ambos os números é: \033[31m{pot}')
        elif num0 == num2:
            pot = num0 * num0

            print(f'A potenciação de ambos os números é: \033[31m{pot}')

    elif choice == 6:
        break
