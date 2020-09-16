# utilizando uma flag
flag = 999
soma = 0 
contador = 0 
n = int(input('digite um número [999 para finalizar]: '))
while n != flag: 
    soma += n  
    contador += 1
    n = int(input('digite um número [999 para finalizar]: '))   
print('Você digitou {} números e a soma entre eles foi {}'.format(contador, soma))

 