#separando dígitos de um número com 4 casas

numero = int(input('digite um número: '))
n = str(numero)
print('Analisando o número {} que você digitou...'.format(n))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

print('_' * 100)

#separando dígitos de um número com 4 casas ou menos
numero = int(input('digite um número: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Analisando o número {} que você digitou...'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))