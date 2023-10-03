# Exercício 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar do valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (Desconsiderando a flag)

# Escrevi a minha própria versão e funcionava perfeitamente, mas acabou que a do professor era melhor. 31/10/2023

cont = soma = 0  # Variável que vai agir como um operando

num = int(input('Digite um número (999 para parar): '))  # Aqui o programa vai pegar a entrada do usuário

while num != 999:  # Enquanto o contador diferir de -1, o programa vai rodar
    soma += num  # Somando os termos
    cont += 1  # Contador vai adicionar +1
    num = int(input('Digite um número (999 para parar): '))  # Caso 999 seja digitado, ele é automaticamente rejeitado
    # da soma

    if num == 999:  # Se o usuário digitar 999, a condição é cumprida e imprime a mensagem abaixo
        print(f'Você digitou {cont} vezes, a soma total é de: {soma}')  # Com a condição cumprida é exibido a soma
