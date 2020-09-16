#jogo pedra-papel-tesoura
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('{:=^60}'.format('Jogo pedra-papel-tesoura'))
print('''Selecione sua opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 20)
print('O Computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-=' * 20)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Você venceu!')
    elif jogador == 2:
        print('O Computador venceu!')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('O Computador venceu!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Você venceu!')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('Você venceu!')
    elif jogador == 1:
        print('O Computador venceu!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')
