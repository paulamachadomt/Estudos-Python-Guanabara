#classificação de triângulos
reta1 = float(input('informe a primeira reta: '))
reta2 = float(input('informe a segunda reta: '))
reta3 = float(input('informe a terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima PODEM formar um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO FORMAM um triângulo.')