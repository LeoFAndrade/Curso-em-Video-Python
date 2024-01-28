# Exercício 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de
# dados para aceitar apenas valores que sejam monetários.

from utilidadescev.dados import leiaDinheiro
from utilidadescev.moeda import resumo

p = leiaDinheiro('Digite o preço: R$')
resumo(p, 10, 15)
