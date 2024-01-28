# Exercício 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
# dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

dados = list()
data = dict()

soma = num = 0

while True:
    data['nome'] = str(input('Nome: ')).capitalize()
    while True:
        data['sexo'] = str(input('Sexo: [M/F] ')).upper()
        if data['sexo'] in 'FfMm':
            break
        print(f'Por favor, digite apenas M ou F')
    data['idade'] = int(input('Digite a idade: '))

    soma += data['idade']
    dados.append(data.copy())  # Aqui será feito uma cópia do dicionário, que será anexado dentro da lista
    while True:
        escolha = str(input('Deseja continuar ? [S/N] ')).upper()
        if escolha in 'SsNn':
            break
        print(f'Por favor, digite apenas S ou N')
    if escolha == 'N':
        break
print('-=-' * 20)
print(f'Foram cadastradas {len(dados)} pessoas !')
media = soma / len(dados)  # Calculando a média
print(f'A média de idade do grupo é de {media:5.2f}')
print('As mulheres cadastradas foram: ')
for p in dados:  # Para cada valor em dados, se o valor dentro da chave "sexo" for um F/f, será exibido o nome que
    # atinge essa condição
    if p["sexo"] in 'Ff':
        print(p["nome"])
print('Lista de pessoas que estão acima da média: ')
for p in dados:  # Semelhante acima, porém se o valor da idade for maior do que a média, será exibido a lista
    # ordenada
    # do dado que atinge a condição
    if p['idade'] > media:
        print('    ')
        for k, i in p.items():  # Para cada chave e valor dentro de 'idade', o programa exibirá o dicionário de
            # forma ordenada
            print(f'  {k} = {i}; ', end='')
            print()
print('<< ENCERRANDO >>')
