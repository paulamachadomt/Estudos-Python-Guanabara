#Verifica se o número é par ou ímpar
num = int(input('digite um número qualquer: '))
if num % 2 == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é ÍMPAR'.format(num))