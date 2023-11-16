# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:início, fim e passo e realize a
# contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):  # O contador vai ter três paramêtros, um serve de início da contagem, o outro fim, e
    # o passo que vai ditar de quanto em quanto deve se contar
    if inicio <= fim:  # Se i início for menor que o fim, a contagem segue um ritmo regular
        cont = inicio  # O inicio vai ser a contagem
        while cont <= fim:  # Até a contagem não for igual a fim, o programa vai continuar contando
            print(f'{cont} ', end='')
            cont += passo  # O contador vai tendo o valor do passo adicionado, até chegar ao 'fim'
            sleep(0.3)
        print('FIM')

    else:  # Se a contagem for ao contrário
        cont = inicio  # Inicia normalmente como no programa acima
        while cont >= fim:  # Enquanto a contagem não for igual a fim, vai continuar até atingir a condição
            print(f'{cont} ', end='')
            cont -= passo  # Aqui o contador vai tendo o valor subtraído, até atingir a condição
            sleep(0.3)
        print('FIM')


print('-=-' * 10)
contador(1, 10, 1)
print('-=-' * 10)
contador(10, 0, 2)
print('-=-' * 10)
contador(inicio=int(input('\nDigite o inicio: ')), fim=int(input('Digite o fim: ')),
         passo=int(input('Digite o passo: ')))
print('-=-' * 10)
