# Exercício 073: Crie uma tupla preenchida com oss 20 primeiros colocados da Tabela do Campeonato Brasileiro de
# Futebol, na ordem de colocação. Depois mostre: A) Apenas os 5 primeiros colocados. B) Os últimos 4 colocados da
# tabela. C) Uma lista com os times em ordem alfabética. D) Em que posição na tabela está o time da Chapecoense.

tabela = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Fluminense', 'Athletico-PR',
          'Atlético-MG', 'São Paulo', 'Cuiabá', 'Internacional', 'Cruzeiro', 'Corinthians', 'Santos', 'Bahia',
          'Vasco da Gama', 'Goiás', 'Coritiba', 'América-MG')

print(f'Lista de times {tabela}')
print('-=' * 50)
print(f'Os 5 primeiros colocados foram: {tabela[0:5]}')
print('-=' * 50)
print(f'Os 5 últimos colocados foram: {tabela[15:21]}')
print('-=' * 50)
print(f'Os times em ordem alfabética: {sorted(tabela)}')
print(f'O Santos está na {tabela.index("Santos")+1}')
