casa = float(input('Qual é o valor da casa ?'))
salario = float(input('Digite o seu salário:'))
ano = float(input('Digite em quantos anos você pretende pagar:'))
meses = ano * 12
pagamento = (casa / meses)
if pagamento > salario * 0.3:
    print('Infelizmente você não pode obter o empréstimo')
else:
    print(f'Empréstimo aprovado, Valor da prestação: R${pagamento:.2f}')
