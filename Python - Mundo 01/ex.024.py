# Exerc�cio 024: Crie um programa que leia o nome de uma cidade e diga se ela come�a ou n�o com o nome "SANTO".

cidade = input('Digite o nome da cidade:').strip().lower()
print(cidade.startswith("santo"))
