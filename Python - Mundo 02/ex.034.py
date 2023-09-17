# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
# salário ou então o empréstimo será negado.

x = '\033[33mAprovando Empréstimo\033[32m'
print(f'\033[32m{x:=^40}\033[m')

casa = float(input('Valor da casa: R$'))
salario = float(input('Digite o salário do cliente: R$'))
anos = int(input('Digite em quantos anos você pretende pagar:'))
meses = anos * 12
pagamento = (casa / meses)
# A multiplicação por decimal facilita a conta.
if pagamento > salario * 0.3:
    print(f'Infelizmente você não pode obter o empréstimo, o valor do empréstimo:\033[31mR${pagamento:.2f}')
else:
    print(f'Empréstimo aprovado, Valor da prestação:\033[32mR${pagamento:.2f}')
