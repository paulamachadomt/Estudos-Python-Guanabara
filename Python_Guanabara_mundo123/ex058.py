#sortear um número
from random import randint
from time import sleep #vai fazer o computador esperar para dar o resultado
computador = randint(0, 10) #faz o computador sortear um número int de 0 a 5
tentativas = 0
acertou = False
print('Sou seu computador...\n Vou pensar em um número entre 0 e 10. Tente adivinhar qual foi...')
while not acertou:    
    jogador = int(input('Qual seu palpite? '))
    print('PROCESSANDO...')
    sleep(1) #dois segundos para o pc mostrar o resultado
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... Tente de novo!')
        elif jogador < computador:
            print('Mais...Tente de novo!')
print('Você acertou após {} tentativas!'.format(tentativas))
