nome = (input('Digite seu nome completo:'))
# O programa exibe informações simples sobre o nome digitado.
print(f'O seu nome em letra minúscula fica como:{nome.upper()}')
print(f'Seu nome em minúsculo fica assim:{nome.lower()}')
print(f'O seu nome tem ao todo: {len(nome) - nome.count(" ")} letras')
separacao = nome.split()
print(f'O seu primeiro nome tem: {len(separacao[0])} letras')
