#cálculo valor a pagar pelos dias alugados de um carro e os km rodados
dias_alugados = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos Km você percorreu com o carro? '))
valor_aluguel = dias_alugados * 60
valor_km = km_rodados * 0.15
valor_total = valor_aluguel + valor_km
print('{} dia(s) de aluguel do carro: R$ {:.2f} reais'.format(dias_alugados, valor_aluguel))
print('{} Km rodados: R$ {:.2f} reais'.format(km_rodados, valor_km))
print('Valor total a pagar: R$ {:.2f} reais'.format(valor_total))
