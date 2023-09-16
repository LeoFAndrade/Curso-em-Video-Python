compra = float(input('Digite o preço das compras: '))
pagamento = int(input("FORMAS DE PAGAMENTO\n"
                      "[ 1 ] À Vista no dinheiro/cheque\n"
                      "[ 2 ] À vista no cartão\n"
                      "[ 3 ] Em 2x no cartão\n"
                      "[ 4 ] Em 3x ou mais no cartão "
                      "\n Digite a sua escolha: "))
if pagamento == 1:
    conta = compra * 0.9
    print(f'O preço ficou R${conta}')
elif pagamento == 2:
    conta = compra * 0.95
    print(f'O preço ficou R${conta}')
elif pagamento == 3:
    conta = compra / 2
    print(f'A compra foi parcelada em 2x de R$ {conta}')
elif pagamento == 4:
    parcela = int(input('Quantas parcelas ? '))
    conta = compra / (parcela * 0.2)
    print(f'A compra foi parcelada em {parcela}x de R${conta} COM juros de 20%')
    print(f'A conta final ficou R${compra + conta}')

else:
    pagamento = int(input("Resposta inválida, por favor escolha uma das opções abaixo:\n"
                          "[ 1 ] À Vista no dinheiro/cheque\n"
                          "[ 2 ] À vista no cartão\n"
                          "[ 3 ] Em 2x no cartão\n"
                          "[ 4 ] Em 3x ou mais no cartão "
                          "\n Digite a sua escolha: "))
