#exibição de números de uma lista sem repetição e em ordem crescente
listanum = []
coninuar = ''
while True:
    num = int(input('digite um valor: '))
    if num not in listanum:
        listanum.append(num)
        print('valor adicionado com sucesso...')
    else:
        print('valor duplicado...')
    continuar = input('deseja continuar? [S/N]').upper()[0]
    while continuar not in 'SN':
        continuar = input('deseja continuar? [S/N]').upper()[0]
    if continuar == 'N':
        print('operação finalizada!')
        break
print('=-' * 30)
listanum.sort()
print(f'você digitou os valores: {listanum}')