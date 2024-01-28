# Exercício Python 044: Elabore um programa que calcule o valor a ser pago
# por um produto, considerando o seu preço normal e condição de pagamento:

# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

z = '\033[33mLojas Leonardo\033[32m'

print(f'\033[32m{z:=^40}\033[m')

compra = float(input('Digite o preço das compras: R$'))
pagamento = int(input("\033[31mFORMAS DE PAGAMENTO\n\033[m"
                      "\033[35m[ 1 ] À Vista no dinheiro/cheque\n"
                      "[ 2 ] À vista no cartão\n"
                      "[ 3 ] Em 2x no cartão\n"
                      "[ 4 ] Em 3x ou mais no cartão\033[m "
                      "\nDigite a sua escolha: "))
if pagamento == 1:
    conta = compra * 0.9
    print(f'O preço ficou\033[32m R${conta:.2f}')
elif pagamento == 2:
    conta = compra * 0.95
    print(f'O preço ficou \033[32mR${conta:.2f}')
elif pagamento == 3:
    conta = compra / 2
    print(f'A compra foi parcelada em 2x de \033[32mR$ {conta:.2f}')
elif pagamento == 4:
    parcela = int(input('Quantas parcelas ? '))
    conta = compra + (compra * 20 / 100)
    total = conta / parcela
    print(f'A compra foi parcelada em {parcela:}x de \033[32mR${total:.2f}\033[m COM juros de 20%')
    print(f'A conta final ficou \033[32mR${conta:.2f}\033[m')

else:
    pagamento = int(input("Resposta inválida, por favor escolha uma das opções abaixo:\n"
                          "[ 1 ] À Vista no dinheiro/cheque\n"
                          "[ 2 ] À vista no cartão\n"
                          "[ 3 ] Em 2x no cartão\n"
                          "[ 4 ] Em 3x ou mais no cartão "
                          "\n Digite a sua escolha: R$"))
