#verifica se a pessoa tem a palavra 'silva' no nome
print('Você tem Silva no sobrenome?')
nome = str(input('digite seu nome completo:')).strip()
print('SILVA' in nome.upper())
