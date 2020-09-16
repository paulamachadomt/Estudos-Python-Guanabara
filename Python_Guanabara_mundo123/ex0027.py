#exibe o primeiro e o último nome da pessoa
n = str(input('digite seu nome completo: ')).strip()
nome = n.split()
print('seu primeiro nome é {} e o último sobrenome é {}'.format(nome[0], nome[len(nome)-1]))

