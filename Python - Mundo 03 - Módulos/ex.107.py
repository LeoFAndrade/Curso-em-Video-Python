# Exercício 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um para que elas aceitem
# um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

from uteis.numeros import moeda

print('~~~' * 20)
print('Calculadora de preço')
print('~~~' * 20)

produto = int(input('Digite o total da compra de produtos R$: '))

print(f'O dobro de {moeda.moeda(produto)} é {moeda.dobro(produto, True)} ')
print(f'Aumentando 10% temos {moeda.aumentar(produto, 10, True)}')
print(f'Reduzindo 20% temos {moeda.diminuir(produto, 20, True)}')
print(f'A metade de {moeda.moeda(produto)} é {moeda.metade(produto, True)}')
