#criação de menu com a repetição while
from time import sleep
opcao = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while opcao != 5:
    print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior valor \n[ 4 ] novos números \n[ 5 ] sair do programa')
    opcao = int(input('>>>>>>>>>digite a opção desejada: '))
    if opcao == 1:
        soma = n1 + n2
        print(soma)
    elif opcao == 2:
        multiplica = n1 * n2
        print(multiplica)
    elif opcao == 3:
        if n1 > n2:
            print(n1)
        else:
            print(n2)
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('opcão inválida. digite novamente')
    print('='*30)
print('Fim do programa!')
