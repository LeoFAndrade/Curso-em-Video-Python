# Exercício 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-lo. Sabendo que cada litro de tinta, pinta uma área de 2m².

l = float(input('Digite a largura da parede:'))
m = float(input('Agora digite a altura:'))
print(f'A dimensão da parede é de {l:.1f}x{m:.1f} e a sua área é de {l*m:.1f}')
print(f'Portanto você precisará de {(l*m)/2:.2f}l de tinta para pintar a parede')
