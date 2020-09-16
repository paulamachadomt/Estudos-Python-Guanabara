#operadores aritméticos: dobro, triplo, raiz quadrada
n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raizqd = n ** (1/2)
print('O dobro de {} é {}'.format(n, dobro))
print('O triplo de {} é {}'.format(n, triplo))
print('A raiz quadrada de {} é {:.2f}'.format(n, raizqd))