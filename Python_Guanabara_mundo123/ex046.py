#contagem regressiva usando o laço for e a função sleep com 0.5 segundos
from time import sleep
for cont in range(10, -1, -1): #contagem de 10 até 0, regressiva
    print(cont)
    sleep(0.5)
print('fim')
