# Exercício 114: Crie um código em Python que teste se o site Pudim está acessível pelo computador.

from urllib.request import urlopen
from urllib.error import *

try:
    Site = urlopen('https://pudim.com.br')
except URLError:
    print('\033[1;31mO Site Pudim não está acessível no momento!')
else:
    print('\033[1;32mO Site Pudim está acessível!')
    print(Site.read())
