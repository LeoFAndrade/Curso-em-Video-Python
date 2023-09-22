# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.


n = int(input('\033[32mDigite um número para saber a sua tabuada:'))  # Aqui o usuário digitará o número desejado
for x in range(1, 11):  # O loop vai iterar de 1 a 10
    print(f'\n\033[32m{n} x {x} = \033[31m{n * x}', end=' ')  # O resultado é calculado com input e loop e exibido
