# Exercício 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas
# eleições.

from datetime import datetime


def voto(data):
    idade = datetime.now().year - data
    if 18 <= idade <= 70:
        return f'Com {idade} anos: O VOTO É OBRIGATÓRIO'

    if 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos: O VOTO É OPCIONAL'

    if idade < 16:
        return f'Com {idade} anos: O VOTO É NEGADO'
    return idade


print(voto(int(input('Digite o ano de nascimento: '))))
