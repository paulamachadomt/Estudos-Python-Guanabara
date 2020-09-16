#exibir os números pares no intervalo de 1 a 50
print('{:=^60}'.format('NÚMEROS PARES'))
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')

#outra forma de resolver diminuindo a quantidade de repetições: ele pula de 2 em 2. Isso poupa tempo de processamento
#for c in range(2, 51, 2):
#   print(c, end=' ')
#print('fim')