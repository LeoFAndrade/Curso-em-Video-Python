# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

cont = 0
soma = 0
media = 0
maior = 0
nome1 = ''
itens = ['masculino', 'feminino']
for x in range(1, 5):
    nome = input(f'Digite o nome da {x}ª pessoa: ')
    idade = int(input(f'Digite a idade {x}ª pessoa: '))
    sexo = input(f'Digite o seu sexo {x}ª pessoa\n [ 1 ] Masculino\n [ 2 ] Feminino\n Digite a opção: ')

    soma = soma + idade
    media = soma / x

    if sexo == '1' and idade > maior:
        maior = idade
        nome1 = nome
    if sexo == '2' and idade < 20:
        cont += 1
print(f'A média de idade do grupo é: {media}')
print(f'O homem mais velho é {nome1}')
if cont == 0:
    print('Não temos mulher(es) no grupo !')

else:
    print(f'Ao todo temos {cont} mulher(es) com menos de 20 anos')
