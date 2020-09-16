lista = []
while True:
    lista.append(int(input('digite um número: ')))
    continuar = str(input('deseja continuar? [S/N]'))
    if continuar in 'Nn':
        break
lista.sort(reverse=True)
print('-=' * 30)
print(f'você digitou {len(lista)} números')
print(f'em ordem decrescente fica assim: {lista}')
if 5 in lista:
    print('O nº 5 está na lista')
else:
    print('O nº 5 não está na lista')