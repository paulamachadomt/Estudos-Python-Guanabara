#calcula o valor da passagem de acordo com a distância da viagem
distancia = float(input('qual a distância em Km da viagem? '))
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print ('Sua viagem de {}km de distância terá uma passagem no valor de R${:.2f} reais'.format(distancia, passagem))
