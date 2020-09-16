#cálculo do comprimento da hipotenusa com a fórmula
cat_oposto = float(input('qual o comprimento do cateto oposto? '))
cat_adj = float(input('qual o comprimento do cateto adjacente? '))
hipotenusa = (cat_oposto ** 2 + cat_adj ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
print ('=' * 100)
print ('=' * 100)

#cálculo do comprimento da hipotenusa com a importação da biblioteca math
import math
cat_oposto = float(input('qual o comprimento do cateto oposto? '))
cat_adj = float(input('qual o comprimento do cateto adjacente? '))
hipotenusa = math.hypot(cat_oposto, cat_adj)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))