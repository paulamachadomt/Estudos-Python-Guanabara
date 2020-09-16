#lista de num pares e ímpares
lista = []
listaPares = []
listaImpares = []
continuar = ''
while True:
    num = int(input('digite um valor: '))
    continuar = input('deseja continuar? S/N ').upper()
    lista.append(num)
    if num % 2 == 0:
        listaPares.append(num)
    elif num % 2 == 1:
        listaImpares.append(num)
    if continuar in 'N':
        break
print(f'você digitou os valores: {lista}')
print(f'Pares: {listaPares}')
print(f'Ímpares: {listaImpares}')