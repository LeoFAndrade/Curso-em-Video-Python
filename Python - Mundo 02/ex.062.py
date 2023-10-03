# Exercício 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar do valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (Desconsiderando a flag)

# Escrevi a minha própria versão e funcionava perfeitamente, mas acabou que a do professor era melhor. 31/10/2023

cont = soma = 0  # Variável que vai agir como um operando

flag = 999  # flag
count = 0  # Contador que vai agir simultaneamente como operando

while count != -1:  # Enquanto o contador diferir de -1, o programa vai rodar

    num = int(input('Digite um número (999 para parar): '))  # O programa só vai parar de perguntar se for digitado 999
    soma = count + num  # Somando os termos
    count = soma  # Transformando o contador para se tornar a soma

    if num == 999:  # Se o usuário digitar 999, a condição é cumprida
        print(f'A soma de todos os números exceto 999 é: {soma-flag}')  # Com a condição cumprida é exibido a soma
        break
