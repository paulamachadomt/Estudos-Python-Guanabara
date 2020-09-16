#exibir 10 primeiros termos de uma progressão aritmética usando WHILE
primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão: '))
termoPA = primeiro
contador = 1
while contador <= 10:
    termoPA = termoPA + razao
    contador += 1
    print('{} -> '.format(termoPA),end='')
print('fim')
