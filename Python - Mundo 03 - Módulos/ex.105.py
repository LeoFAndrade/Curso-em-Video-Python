# Exercício 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e
# metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from uteis.numeros import moeda

print('~~~' * 20)
print('Calculadora de preço')
print('~~~' * 20)
produto = int(input('Digite o total da compra de produtos R$: '))
print(f'O dobro de {produto} é R$ {moeda.dobro(produto)} ')
print(f'Aumentando 10% temos R$ {moeda.aumentar(produto, 10)}')
print(f'Reduzindo 20%, temos R$ {moeda.diminuir(produto, 20)}')
print(f'A metade de {produto} é R$ {moeda.Metade(produto)}')
