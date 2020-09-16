#indica se a pessoa ultrapassou ou não o limite de velocidade
velocidade = int(input('qual é a velocidade do carro em km/h? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTA! você ultrapassou o limite de velocidade (80Km/h) e será multado!') 
    print('Sua multa será no valor de R${} reais.'.format(multa))
else:
    print('boa viagem e dirija em segurnça!')