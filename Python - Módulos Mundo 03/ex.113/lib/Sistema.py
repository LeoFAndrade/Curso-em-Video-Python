def Cadastro():
    nome = str(input('NOME: '))
    idade = input('IDADE: ')

    arquivo = open('Tabela', 'a')
    dado = [nome, ';', idade, '\n']
    arquivo.writelines(dado)
    arquivo.close()
