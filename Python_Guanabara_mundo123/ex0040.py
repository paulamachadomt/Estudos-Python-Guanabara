#cálculo da média do aluno
nota1 = float(input('informe a primeira nota do aluno: '))
nota2 = float(input('informe a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print('Com as notas {:.1f} e {:.1f}, a média do aluno é: {:.1f}'.format(nota1, nota2, media))
if media >= 7:
    print('O aluno está APROVADO')
elif media >= 5 and media < 7:
    print('O aluno está em RECUPERAÇÃO')
elif media < 5:
    print('O aluno está REPROVADO')