# Exercício Python 048: Faça um programa que calcule a soma entre todos os
# números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
contador = 0
for x in range(0, 501):  # Os números vão de 0 a 500
    if x % 2 == 1:  # Aqui se calculará usando o resto da divisão, nesse caso oos números ímpares
        if x % 3 == 0:  # A mesma coisa acima, porém usando para obter os números ímpares múltiplos de 3
            soma += x
            contador += +1
print(f'A soma de todos os números ímpares divisíveis por três é:'
      f' {soma}, O número de vezes que foi contado é {contador}')
