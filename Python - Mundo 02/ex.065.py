# Exercício 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
# entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = quant = media = maior = menor = 0  # Variáveis
resp = 's'  # Variável

while resp in 'Ss':  # Enquanto a resposta for "Sim" ou "S/s" o programa vai rodar
    num = int(input('Digite um número: '))  # Entrada do usuário
    quant += 1  # Toda vez que o usuário der uma entrada o contador soma +1
    soma += num  # Os números digitados se somam na variável "soma"
    media = soma / quant  # Com a soma e quantidade de entradas do usuário que são equivalentes, a média é calculada

    if quant == 1:
        maior = menor = num  # Juntado todas as variáveis
    else:
        if num > maior:  # Se o número for "maior" que o "maior", ele se torna o "maior"
            maior = num  # Maior
        if num < menor:  # A mesma lógica de acima, porém com o menor valor
            menor = num  # Menor
    resp = str(input('Quer continuar? [S/N]: ')).upper()[0]  # O usuário tem a opção continuar o programa

print(f'A média entre os números é de {media}')
print(f'O maior número lido é {maior} e o menor lido é {menor}')
