cor = ['\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m']


def Cabeçalho(msg):
    print('\033[1m-' * 42)
    print(f'{msg.center(42)}')
    print('-' * 42)


def Menu(Lista):
    Cabeçalho('MENU PRINCIPAL')
    print(f'{cor[3]}1 - {cor[4]}Ver pessoas cadastradas')
    print(f'{cor[3]}2 - {cor[4]}Cadastrar nova Pessoa')
    print(f'{cor[3]}3 - {cor[4]}Sair do Sistema\033[m')
    print('\033[1m---' * 15)
    while True:
        escolha = input(f'{cor[2]}Sua Opção: \033[m')
        if escolha in '1':
            Cabeçalho('PESSOAS CADASTRADAS')
            print(Lista)
        elif escolha in '2':
            Cabeçalho('CADASTRO')
        elif escolha in '3':
            print('Obrigado e até a próxima!')
            break
        else:
            print(f'{cor[1]}Por favor digite um número válido\033[m')


X = Menu([1,2,3,4])
print(X)
