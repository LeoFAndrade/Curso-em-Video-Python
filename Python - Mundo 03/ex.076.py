# Exercício 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Arroz', 15.00, 'Carne', 25.00, 'Cereal', 2.00, 'Manteiga', 3.50, 'Café', 4.00,
            'Pão', 1.50, 'Feijão', 7.00, 'Leite', 2.50, 'Batata', 4.00, 'Alface', 5.00)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<40}', end='')
    elif pos % 2 != 0:
        print(f'R${produtos[pos]:.2f}')
