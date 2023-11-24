# Exercício 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função


# noinspection NonAsciiCharacters
def notas(*nota, sit=False):
    """⇾ Função que analisa notas de um grupo de alunos.

    :param: *nota: As notas que serão analisadas (Aceita quantas forem necessárias)
    :param  sit: Valor que indica se a situação dos alunos deve ser exibida ou não (Opcional)
    :return: Exibe um dicionário com as informações analisadas do grupo de notas"""

    dicionario = dict()
    dicionario['Total'] = len(nota)
    dicionario['Maior'] = max(nota)
    dicionario['Menor'] = min(nota)
    dicionario['Media'] = sum(nota)/len(nota)
    if sit:
        if dicionario['Media'] >= 7:
            dicionario['Situação'] = 'BOA'
        elif dicionario['Media'] >= 5:
            dicionario['Situação'] = 'RAZOÁVEL'
        else:
            dicionario['Situação'] = 'RUIM'
    return dicionario


# Programa principal
resp = notas(4.5, 4.3, 6.8, 9.9, 9.0, 7.4, sit=True)
print(resp)
help(notas)
