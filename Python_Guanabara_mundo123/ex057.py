#validação de dado digitado pelo usuário
sexo = str(input('informe o sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('dados inválidos. verifique e digite novamente.')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))