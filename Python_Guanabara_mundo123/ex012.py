#cálculo de desconto no valor de um produto
preco = float(input('Digite o valor do produto: R$'))
desconto = preco * 0.05 #
novo_preco = preco - desconto
print('O produto que custava R$ {:.2f} reais passa a custar R$ {:.2f} reais (com 5% de desconto)'.format(preco, novo_preco))

# outra forma de conceder o desconto: novo_preco = preco - (preco * 5 / 100)

