#verifica se o nome da cidade digitada começa com a palavra 'santo'
cidade = str(input('digite o nome de uma cidade:')).strip()
print(cidade[:5].upper() == 'SANTO')

