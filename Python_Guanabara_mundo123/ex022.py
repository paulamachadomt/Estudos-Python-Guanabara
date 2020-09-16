#manipulação de strings: maiúscula, minúscula, contagem de caracteres sem os espaços, selecionar apenas o primeiro nome

nome = str(input('digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas fica:', (nome.upper()))
print('Seu nome em minúsculas fica: ', (nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
primeiro_nome = nome.split()
print(nome.split())
print('Seu primeiro nome é {}, que tem {} letras'.format(primeiro_nome[0], len(primeiro_nome[0])))
