num = (int(input('digite um número: ')), 
      int(input('digite outro número: ')),
       int(input('digite mais um número: ')), 
       int(input('digite o último número: ')))
print(f'Você digitou os números: {num}') 
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('o valor 3 não foi digitado')
print(f'Os números pares digitados foram: ', end='') 
for n in num:
    if n % 2 == 0:
        if  num.index(n) == 3:
            print(n, end=' ')
        else:
            print(n,',', end=' ')
     