n = input('Digite qualquer coisa')
print('Tipo primitivo;', type(n)), print('É numérico ?', n.isnumeric()), print('É alfabético ?', n.isalpha())
print('É alfanumérico ?', n.isalnum()), print('É decimal ?', n.isdecimal()), print('Está em maiúsculo ?', n.isupper())
print('Está em minusculo ?', n.islower()), print('Está capitalizada ?', n.istitle())
print('Só tem espaços ?', n.isspace())