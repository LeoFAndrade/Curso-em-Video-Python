nota1 = float(input('Digite a primeira nota do aluno:'))
nota2 = float(input('Digite a segunda nota do aluno:'))
media = (nota1 + nota2)/2
print(f'A média de notas foi {media}')
if media >= 7.0:
    print('\033[32mParabéns você passou!!!')
elif 5.0 <= media <= 6.9:
    print('\033[33mVocê está de recuperação!!!')
elif media < 5.0:
    print('\033[31mVocê foi reprovado!!!')
