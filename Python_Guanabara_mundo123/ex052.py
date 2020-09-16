#informar se o número é primo
num = int(input('digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total = total + 1
print('O número {} foi divisível {} vezes'.format(num, total))       
if total == 2:
    print('É um número primo.')
else:
    print('NÃO é um número primo.')


    
