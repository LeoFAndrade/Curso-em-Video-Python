# Exercício 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correto.

lista = []
lista1 = str(lista).strip('[]')

try:  # Fluxo de controle, permite testar e lidar com códigos, inclusive os que podem dar erro
    expressao = str(input('Digite uma expressão matemática: '))
    lista.append(expressao)  # Adicionando a expressão à lista

    resposta = eval(expressao)  # Analisando se a expressão é Verdadeira ou Falsa

    lista1 += expressao  # Concatenando os valores
    if resposta:  # Se a resposta for válida, ele retorna a mensagem de validação
        print(f'A expressão {expressao} é verdeira!')

except SyntaxError:  # Se a sintaxe estiver incorreta, o programa retorna uma mensagem de erro.
    print(f'A expressão {lista1} é falsa!')
