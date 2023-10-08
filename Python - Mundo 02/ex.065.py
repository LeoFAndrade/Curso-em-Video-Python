# Exercício 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
# usuário. O programa será interrompido quando o número solicitado for negativo

num = 0  # Variável

print('Quer ver a tabuada de qual valor ? ')
print('Digite um valor negativo para parar!')

while num >= 0:  # Enquanto o número for maior que 0, o programa vai continuar
    print(f'\033[31m---' * 20)
    num = int(input('\033[32mDigite um número:'))  # Entrada do usuário
    print(f'\033[31m---' * 20)

    for x in range(1, 11):  # entre 1 e 10 vai ocorrer uma iteração sobre todos os elementos
        if num < 0:  # Se o número for negativo, o programa para
            break  # Parada
        print(f'\n\033[32m{num} x {x} = \033[31m{num * x}')  # Multiplicação das tabuadas
print('\033[32mPrograma tabuada encerrado. volte sempre.')
