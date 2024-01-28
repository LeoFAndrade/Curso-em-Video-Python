# Exercício 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
# qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
# entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

# noinspection NonAsciiCharacters
cedula = 50  # Começamos com a nota de maior valor
print('=' * 30)
print('{:^30}'.format('BANCO LEONARDO'))
print('=' * 30)

dinheiro = int(input('Que valor você quer sacar ? R$'))  # Entrada do usuário
total = dinheiro  # Variável que vai converter para o valor do usuário
totced = 0


while True:
    if total >= cedula:  # Se o total for igual ou maior que a cédula de 50, ele subtrairá o valor e a cédula
        total -= cedula
        totced += 1  # Será adicionado +1 ao contador a cada nota de R$50

    else:  # Caso contrário, a variável vai se converter conforme o necessário
        if totced > 0:  # Se o total de cédulas não for maior que 0, então o programa nem conta
            print(f'Foi no total {totced} cédulas de R${cedula}')  # Aqui o print vai iterar sobre o resto do código
        if cedula == 50:
            cedula = 20  # Assim o programa vai comparando se cada nota é igual ou maior e vai adicionando +1 ao totced
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if total == 0:
            print('Volte sempre ao BANCO LEONARDO, TENHA UM BOM DIA!')
            print('=' * 30)
            break
# Esse eu acabei ficando sem ideia realmente de como fazer e acabei copiando do professor tudo mesmo. 12/10/2023 16:19
