# Exercício 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
# em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o
# salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

Pessoa = dict()

Pessoa['Nome'] = str(input('Nome: '))
Data = int(input('Data de nascimento: '))
Pessoa['Idade'] = datetime.now().year - Data  # Calculando a idade pegando o ano atual e subtraindo o da data de nasc
Pessoa['CTPS'] = int(input('Carteira de Trabalho [0 se não tiver]: '))

if Pessoa['CTPS'] != 0:  # Se o valor da CTPS for diferente de 0, o programa continua rodando
    Pessoa['Contratação'] = int(input('Ano de contratação: '))
    Pessoa['Salário'] = float(input('Salário: R$'))
    Pessoa['Aposentadoria'] = Pessoa['Idade'] + (Pessoa['Contratação'] + 35) - datetime.now().year  # Aqui pega a idade
    # faz adição com o ano de contratação com + 35 anos e subtrai com o ano atual
print('-=-' * 15)
for i, v in Pessoa.items():
    print(f' - {i} tem o valor de {v}')
