#cálculo de seno, cosseno e tangente com módulo math
from math import radians, sin, cos, tan
angulo = int(input('digite o valor de um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('o ângulo de {} graus tem o seno {:.2f}, cosseno {:.2f} e a tangente {:.2f}.'.format(angulo, seno, cosseno, tangente))
