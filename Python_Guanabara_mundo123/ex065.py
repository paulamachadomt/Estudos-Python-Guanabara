
#maior e menor 
n = media = contador = soma = maior = menor = 0
opcao = 'S'
while opcao in 'Ss':
    n = int(input('digite um número: '))
    opcao = str(input('deseja continuar? [S/N] ')).upper().strip()[0]
    contador += 1
    soma += n
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / contador
print('Você digitou {} valores e a média entre eles foi de {:.2f}'.format(contador, media))
print('o maior valor digitado foi {} e o menor {}'.format(maior, menor))
