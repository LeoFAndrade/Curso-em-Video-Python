# Exercício 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetro: o primeiro que indique o
# número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na
# tela o processo de cálculo do fatorial.

# noinspection NonAsciiCharacters
def fatorial(número=1, show=False):
    """ → Calcula o fatorial de um número.
    :param número: O número a ser calculado
    :param show: (opcional) Exibe ou não a conta (Vem 'False' por padrão)
    :return: O valor do Fatorial de um número 'número'"""

    fact = 1  #
    for num in range(número, 0, -1):   # O programa começa com o número provido pelo usuário e vai regressando a cada um
        fact *= num  # Cada número vai ser multiplicado e se tornar o novo resultado simultaneamente, até chegar à '1'
        if show is True:  # O usuário tem a opção de optar em ver a conta
            print(f'{num}', 'x ' if num > 1 else '= ', end='')
    print(fact)  # O resultado do fatorial vai ser exibido
    return fact  # O resultado vai ser retornado ao 'chamador'


fatorial(5, True)
