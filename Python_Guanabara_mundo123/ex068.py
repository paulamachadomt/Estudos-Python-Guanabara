from random import randint
jogador = soma = contador = 0
opcao = " "
while True:
    computador = randint(0,10)
    jogador = int(input('Digite um valor: '))
    soma = jogador + computador
    while opcao not in 'PpIi':
        opcao = input('Par ou ímpar? [P / I] ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}')
    if soma % 2 == 0:
        print('DEU PAR')
        if opcao == 'P':
            print('VOCÊ VENCEU!')
            contador =+ 1
        else:
            print('VOCÊ PERDEU!')
            break
    else:
        print('DEU ÍMPAR')
        if opcao == 'I':
            print('VOCÊ VENCEU!')
            contador =+ 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('-' * 60) 
if contador == 0:
    print('GAME OVER! Você não ganhou nenhuma vez!')
else:
    print(f'GAME OVER. Você ganhou {contador} vezes.')
    