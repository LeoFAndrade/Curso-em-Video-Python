# Exercício 110: Adicione ao módulo moeda.py criado nos desafios anteriores,
# uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo
# criado até aqui.
from uteis.numeros import moeda


num = int(input('Digite um número:'))
moeda.resumo(num, 50, 25)
