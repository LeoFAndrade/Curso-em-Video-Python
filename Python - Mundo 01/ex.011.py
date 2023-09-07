produto = float(input('Digite o preço do produto:'))
desconto = float(input('Digite a porcentagem do desconto:'))
# Verificando o preço final do produto com desconto.
print(f'O preço do produto com desconto é:{produto-(produto*desconto/100):.2f}R$')
