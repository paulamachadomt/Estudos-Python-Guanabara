#cálculo para conceder finaciamento de acordo com o comprometimento da renda mensal
preco_casa = float(input('informe o valor da casa que deseja comprar: R$ '))
salario = float(input('informe o seu salário: R$ '))
anos_pagamento = int(input('informe em quantos anos deseja pagar o imóvel: '))
prestacao = preco_casa / anos_pagamento / 12
if prestacao > salario * 30 / 100:
    print('FINANCIAMENTO NEGADO! A prestação será de R${:.2f} reais e compromete mais de 30% de sua renda.'.format(prestacao))
else:
    print('FINANCIAMENTO ACEITO! A prestação será no valor de R${:.2f} reais.'.format(prestacao))