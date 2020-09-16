#gerenciador de pagamentos
print('{:=^40}'.format('LOJA COSMOS'))
valor_compra = float(input('Informe o valor da sua compra: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção?'))
if opcao == 1:
    desconto_1 = valor_compra - (valor_compra * 10 / 100)
    print('Sua compra no valor de R${:.2f} sairá por R${:.2f}'.format(valor_compra, desconto_1))
elif opcao == 2:
    desconto_2 = valor_compra - (valor_compra * 5 /100)
    print('Sua compra no valor de R${:.2f} sairá por R${:.2f}'.format(valor_compra, desconto_2))
elif opcao == 3:
    print('Sua compra no valor de R${:.2f}, paga em 2x sem juros, sairá por R${:.2f} (R${:.2f} reais cada parcela)'.format(valor_compra, valor_compra, valor_compra / 2))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    desconto_4 = valor_compra + (valor_compra * 20 /100)
    valor_parcela = desconto_4 / parcelas
    print('Sua compra no valor de R${:.2f}, paga em {:.2f} parcelas, sairá por R${} no total com juros, sendo cada parcela no valor de R${}'.format(valor_compra, parcelas, desconto_4, valor_parcela))
else:
    print('Opção inválida. Verifique e tente novamente.')
