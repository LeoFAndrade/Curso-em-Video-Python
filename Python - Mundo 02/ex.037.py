from datetime import date
datahj = date.today().year
data = int(input('Digite a data de nascimento:'))
idade = datahj - data
print(f'Quem nasceu em {data}, tem {idade} anos')
if idade == 18:
    print('É hora de se alistar')
elif idade < 18:
    print('Ainda vai se alistar')
elif idade > 18:
    print('Já passou da hora se alistar')
