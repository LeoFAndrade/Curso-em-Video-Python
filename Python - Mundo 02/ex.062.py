# Exercício 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar do valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (Desconsiderando a flag)


flag = 999  # flag
cont = soma = 0   # Variável que vai agir como um operando


num = int(input('Digite um número (999 para parar): '))
while num != 999:  # Enquanto o contador diferir de -1, o programa vai rodar
    soma += num  # Somando os termos
    num = soma  # Transformando o contador para se tornar a soma
    cont += 1
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:  # Se o usuário digitar 999, a condição é cumprida
        print(f'Você digitou {cont} vezes, a soma total é de: {soma}')  # Com a condição cumprida é exibido a soma

