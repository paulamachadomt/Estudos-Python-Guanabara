#análise em grupo de pessoas
contHomens = maiores18 = mulheres20 = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Deseja cadastrar mais uma pessoa? [S/N] ').strip().upper()[0]
    if idade > 18:
        maiores18 += 1
    if sexo == 'M':
        contHomens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1   
    if opcao == 'N': 
        break
print('{:-^60}'.format(' RESULTADO '))
print(f'Total de pessoas com mais de 18 anos: {maiores18}')
print(f'Homens cadastrados: {contHomens}')
print(f'Mulheres com menos de 20 anos: {mulheres20}')
