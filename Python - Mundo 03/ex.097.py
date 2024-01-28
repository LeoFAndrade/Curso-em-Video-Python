# Exercício 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
# mostre uma mensagem com tamanho adaptável.
# EX: escreva('Olá, Mundo!')
# Saída: ~~~~~~~~~~~~
#         Olá Mundo!
#        ~~~~~~~~~~~~

def escreva(palavra):
    tamanho = len(palavra) + 4
    print('~' * tamanho)
    print(f'  {palavra}')
    print('~' * tamanho)


escreva(palavra=str(input('Digite uma palavra: ')))
# Assim como o primeiro dos exercícios desta aula de funções, eu consegui fazer sozinho, exceto que desta vez eu
# precisei de ajuda no finalzinho.
