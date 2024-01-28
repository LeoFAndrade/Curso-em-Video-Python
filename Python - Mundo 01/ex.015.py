# Exercício 015: Escreva um programa que pergunte a quantidade KM percorridos por um carro alugado e a quantidade de
# dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15
# por KM rodado.

dia = int(input('Por quantos dias o carro foi alugado ?'))
km = float(input('Quantos Km foram rodados ?'))
# Calculando o valor total a ser pago.
pago = (dia * 60) + (km * 0.15)
