#somar os números ímpares e múltiplos de 3 no intervalo de 1 a 500
soma = 0 #acumulador vai somando os valores: +c
contador = 0 #contador vai contando os valores: +1
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1
    soma = soma + c
print('A soma de todos os {} valores ímpares múltiplos de 3 no intervalo entre 1 e 500 é: {}'.format(contador, soma))