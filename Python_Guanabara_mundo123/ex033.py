#indica qual dos valores digitados é o maior e o menor
valor1 = int(input('digite um número: '))
valor2 = int(input('digite outro número: '))
valor3 = int(input('digite outro número: '))
#verificando quem é o menor
menor = valor1
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3
#verificando qual é o valor maior
maior = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor1 and valor3 > valor2:
    maior = valor3
print('o menor valor digitado foi {}.'.format(menor))
print('o maior valor digitado foi {}.'.format(maior))