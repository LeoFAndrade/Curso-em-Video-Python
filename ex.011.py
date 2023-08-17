p = float(input('Digite o preço do produto:'))
d = float(input('Digite a porcentagem do desconto:'))
print(f'O preço do produto com desconto é: {p-(p*d/100):.2f}R$')
