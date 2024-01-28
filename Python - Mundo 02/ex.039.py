# Exercício Python 039: Faça um programa que leia o ano de nascimento de um
# jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao
# serviço militar, se é a hora exata de se alistar ou se já passou do tempo
# do alistamento. Seu programa também deverá mostrar o tempo que
# falta ou que passou do prazo.

# Usando da biblioteca date para fins de informação do tempo
from datetime import date


# Usando a data atual para calcular o tempo desde o nascimento
atual = date.today().year
data = int(input('Digite a data de nascimento:'))
idade = atual - data
saldo = 18 - idade
# Classificando o alistante conforme a idade apresentada
print(f'Quem nasceu em \033[34m{data}\033[m, tem \033[34m{idade} anos')
if idade == 18:
    print('\033[33mÉ hora de se alistar.')
elif idade < 18:
    ano = atual + saldo
    print(f'\033[32mAinda falta {saldo} ano para o seu alistamento.')
    print(f'\033[32mSeu alistamento será em {ano}')
elif idade > 18:
    print('\033[31mJá passou da hora se alistar.')
    saldo = idade - 18
    anos = atual - saldo
    print(f'\033[31mSeu alistamento deveria ter sido no ano de {anos}')
