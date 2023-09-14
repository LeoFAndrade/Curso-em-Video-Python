from datetime import date

atual = date.today().year
nasc = int(input('Digite a data de nascimento:'))
idade = atual - nasc
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
