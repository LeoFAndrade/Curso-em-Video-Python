# Exercício 108: Adapte o código do desafio 107, criando uma função adicional que consiga mostrar os valores como um
# valor monetário formatado.

from uteis.numeros import moeda

print('~~~' * 20)
print('Calculadora de preço')
print('~~~' * 20)

produto = int(input('Digite o total da compra de produtos R$: '))

print(f'O dobro de {moeda.moeda(produto)} é {moeda.moeda(moeda.dobro(produto))} ')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(produto, 10))}')
print(f'Reduzindo 20% temos {moeda.moeda(moeda.diminuir(produto, 20))}')
print(f'A metade de {moeda.moeda(produto)} é {moeda.moeda(moeda.metade(produto))}')
