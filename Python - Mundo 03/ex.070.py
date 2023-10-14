# Exercício 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até
# vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')  # Tupla

while True:  # Repetição infinita
    numero = int(input('Digite um número de 0 a 20: '))  # Entrada do usuário
    if 0 <= numero <= 20:  # Se o número for abaixo de 0 ou acima de 20, o programa imprime uma mensagem
        break
    print('Tente novamente,', end=' ')  # Se a condição de cima não se cumprir, o programa pede novamente até se cumprir
print(f'O número digitado por extenso é {extenso[numero]}')  # O 'numero' dentro dos colchetes pega a localização do
# item da tupla 'extenso'
