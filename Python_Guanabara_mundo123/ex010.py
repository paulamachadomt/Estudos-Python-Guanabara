#conversão de medidas: real, dólar
dinheiro = float(input('Quantos reais você tem? '))
dolar_convert = dinheiro / 4.35
euro_convert = dinheiro / 4.73
print('Com essa quantia (R$ {} reais) você pode comprar US$ {:.2f} dólares ou £ {:.2f} euros'.format(dinheiro, dolar_convert, euro_convert))