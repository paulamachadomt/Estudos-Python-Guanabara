#cálculo de uma área em m2 e a quantidade de tinta necessária
largura = float(input('Informe a largura da parede em metros: '))
altura = float(input('Informe a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('Para pintar a área total de {} metros quadrados serão necessários {} litros de tinta.'.format(area, tinta))
