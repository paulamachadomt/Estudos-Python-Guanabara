somaidade = 0
mediaIdade = 0
maiorIdadeHomem =0
nomeVelho = ''
totMulher20 = 0
for pessoa in range(1,5):
    print('---------- {}ª PESSOA ----------'.format(pessoa))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    genero = str(input('Sexo [F/M]: '))
    somaidade += idade #média de idade do grupo todo
    if pessoa == 1 and genero in 'Mn':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if genero in 'Mn' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if genero in 'Ff' and idade < 20:
        totMulher20 += 1
mediaIdade = somaidade / 4
print('Média de idade do grupo: {} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdadeHomem, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totMulher20))
