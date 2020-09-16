#exibir 10 primeiros termos de uma progressão aritmética usando WHILE
primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão: '))
termoPA = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        termoPA = termoPA + razao
        contador += 1
        print('{} -> '.format(termoPA),end='')
    print('PAUSA')
    mais = int(input('quantos termos você quer mostrar a mais?'))
print('progressão finalizada com {} termos'.format(total))