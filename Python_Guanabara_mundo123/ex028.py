#sortear um número
from random import randint
from time import sleep #vai fazer o computador esperar para dar o resultado
computador = randint(0, 5) #faz o computador sortear um número int de 0 a 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2) #dois segundos para o pc mostrar o resultado
if computador == jogador:
    print('Você adivinhou!')
else:
    print('Você errou! Eu pensei no número {} e não no {}!'.format(computador, jogador))
