#conversão de medidas: metros para centímetros e milímetros
metros = float(input('Quantos metros? '))
cm_convert = metros * 100
mm_convert = metros * 1000
print('{:.1f} metros equivalem a {:.1f}cm e {:.1f}mm'.format(metros, cm_convert, mm_convert))