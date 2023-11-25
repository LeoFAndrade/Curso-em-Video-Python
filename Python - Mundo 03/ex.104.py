# Exercício 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
# manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# OBS: Use cores.

c = ['\033[41m',  # Fundo vermelho - 0
     '\033[42m',  # Fundo verde - 1
     '\033[43m']  # Fundo amarelo - 2
c0 = '\033[m'


def Ajuda(com):
    título('Acessando o manual do comando', 2)
    help(com)


# noinspection NonAsciiCharacters
def título(msg, cor=0):
    tam = len(msg) + 4
    print(f'{c[cor]}')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHelp', 1)
    comando = str(input('Função ou Biblioteca > '))
    título(comando, 2)
    if comando.upper() == 'FIM':
        break
    else:
        Ajuda(comando)
título('Até mais', 0)
