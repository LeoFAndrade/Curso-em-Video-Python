# Exercício 066: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar do valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (Desconsiderando a flag)

soma = cont = 0  # Variáveis de controle

while True:  # Loop infinito

    num = int(input('Digite umm número [999 para parar]: '))  # Entrada do usuário
    if num == 999:  # Se o número que o usuário digitou for 999, o programa para
        break  # Parada
    cont += 1  # Aqui as variáveis estão no laço do loop infinito, no laço "while True"
    soma += num  # Soma
print(f'A soma dos {cont} valores foi de: {soma}!')
