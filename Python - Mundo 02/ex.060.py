# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

x = 'Fatorial'
print(f'{x:=^40}')

num = int(input('Digite um número: '))  # Entrada do usuário
c = num  # Variável
f = 1  # Fatorial
while c > 0:  # Enquanto a variável for maior que 0, o programa vai repetir
    print(f'{c} ', end='')  # A variável c vai ser exibida até o loop acabar
    print(f'x ' if c > 1 else '= ', end='')  # Se a variável c for maior que 1, ele vai exibir "x" se não "="
    f *= c  # cálculo do fatorial
    c -= 1
print(f)
