def Cadastro(msg):
    data = []
    nome = str(input(msg))
    while True:
        try:
            idade = int(input('Digite a idade: '))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')

        except KeyboardInterrupt:
            print('\033[1;33mEntrada de valor interrompida pelo usuário!\033[m')
            break

x = Cadastro('Digite o nome: ')
