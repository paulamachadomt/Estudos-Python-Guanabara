#exibir a porção inteira de um número
#trunc = retira a parte quebrada do número

import math
num = float(input('Digite um número: '))
print('A porção inteira de {} é {}'.format(num, math.trunc(num)))

print("=" * 20)

#outra forma de resolver, importando apenas o trunc
from math import trunc
num = float(input('digite um número: '))
print('A porção inteira de {} é {}'.format(num, trunc(num)))

print("=" * 20)

#outra forma, sem precisar importar a biblioteca math, usando apenas int
num = float(input('digite um número: '))
print('A porção inteira de {} é {}'.format(num, int(num)))
