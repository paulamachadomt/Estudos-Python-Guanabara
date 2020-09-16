from math import factorial
from time import sleep
num = int(input('digite um número para calcular seu fatorial: '))
contador = num
fatorial = 1
print('calculando o fatorial de {}...'.format(num))
sleep(2)
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador
    contador = contador - 1
print(fatorial)

