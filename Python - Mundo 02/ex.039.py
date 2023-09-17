# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, conforme a idade:

# Usando a biblioteca date para fins de informação sobre o tempo
from datetime import date

# Calculando a partir do dia do nascimento até o dia atual
atual = date.today().year
nasc = int(input('Digite a data de nascimento:'))
idade = atual - nasc
# Classificando o atleta conforme a idade atual
if idade <= 9:
    print('A categoria é: \033[34mMIRIM')
elif idade <= 14:
    print('A categoria é: \033[36mINFANTIL')
elif idade <= 19:
    print('A categoria é: \033[33mJUNIOR')
elif idade <= 25:
    print('A categoria é: \033[31mSÊNIOR')
elif idade > 25:
    print('A categoria é: \033[35mMASTER')
