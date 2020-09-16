#Soma de números pares
print('{:=^60}'.format("SOMA DE NÚMEROS PARES"))
soma = 0
contador = 0
for c in range(1,7):
    num = int(input('digite um valor: '))
    if num % 2 == 0:
        soma = soma + num
        contador = contador + 1
print('Você digitou {} números pares e o resultado da soma entre eles é {}'.format(contador, soma))

