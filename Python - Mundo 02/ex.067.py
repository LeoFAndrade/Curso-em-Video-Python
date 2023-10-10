# Exercício 069: Crie um programa que leia a idade eo sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos

maioridade = contador = menoridade = 0
x = 'CADASTRE UMA PESSOA'

while True:
    print('\033[1;35m-=' * 20)
    print(f'\033[1;33m{x:^40}')
    print('\033[1;35m-=\033[32m' * 20)

    idade = int(input('Idade: '))  # Entrada do usuário
    sexo = ' '
    if idade > 18:
        maioridade += 1

    while sexo not in 'MF':  # Usando a estrutura de repetição while, enquanto a condição não for atingida, se repetirá
        sexo = str(input('Sexo[M/F]: ')).upper()[0]

        if sexo == 'M':
            contador += 1

        if sexo == 'F' and idade < 20:
            menoridade += 1
    resp = ' '
    while resp not in 'SN':  # A mesma lógica da variável 'sexo' acima
        resp = str(input('Deseja continuar ? [S/N]: ')).upper()[0]
    if resp == 'N':
        break
print(f'temos {maioridade} maiores de 18 anos!')
print(f'Temos {contador} homens cadastrados no total!')
print(f'Temos {menoridade} mulheres menores de 20 anos!')
