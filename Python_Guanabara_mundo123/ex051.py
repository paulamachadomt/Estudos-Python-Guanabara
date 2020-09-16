#exibir 10 primeiros termos de uma progressão aritmética usando o FOR
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(' {} '.format(c), end=' -> ')
print('FIM')

