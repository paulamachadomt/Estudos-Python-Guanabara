#análise de lista de compras
totCompra = prodMil = menor = contador = 0
barato = ' '
while True:
    print('{:-^100}'.format(' LISTA DE COMPRAS '))
    produto = input('Nome do produto: ')
    preco = float(input('Preço do produto: '))
    contador += 1
    totCompra += preco
    if preco > 1000:
        prodMil += 1
    if contador == 1:
        menor = preco
        barato = produto
    elif preco < menor:
        menor = preco
        barato = produto
    opcao = ' '
    while opcao not in "SN":
        opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
    if opcao == 'N':
        break 
print('{:-^100}'.format(' PROGRAMA FINALIZADO '))   
print(f'O total da compra foi de R${totCompra:.2f}')
print(f'Há {prodMil} produto(s) custando mais de R$1mil.')
print(f'O produto mais barato foi {barato}, que custou R${menor:.2f}')