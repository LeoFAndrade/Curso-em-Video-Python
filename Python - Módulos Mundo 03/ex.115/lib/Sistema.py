def Cadastro():
    nome = str(input('NOME: '))
    while True:
        try:
            idade = int(input('IDADE: '))
        except (ValueError, TypeError):
            print('\033[1;31mPor favor, digite um valor válido!\033[m')
            continue
        else:
            idade = str(idade)
            arquivo = open('Lista.txt', 'a')
            dado = [f"{nome}       {idade:>22} \n"]
            arquivo.writelines(dado)
            arquivo.close()
        break
