casa = float(input('Valor da casa: R$'))
salario = float(input('Digite o salário do cliente: R$'))
anos = int(input('Digite em quantos anos você pretende pagar:'))
meses = anos * 12
pagamento = (casa / meses)
# A multiplicação por decimal facilita bastante a conta.
if pagamento > salario * 0.3:
    print(f'Infelizmente você não pode obter o empréstimo, o valor do empréstimo: R${pagamento:.2f}')
else:
    print(f'Empréstimo aprovado, Valor da prestação: R${pagamento:.2f}')
