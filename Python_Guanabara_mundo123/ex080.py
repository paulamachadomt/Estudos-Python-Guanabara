#implementação na mão da função sort -> lista de nºs ordenados cresc
listanum = []
for c in range (0,5):
    num = int(input('digite um número: '))
    if c == 0 or num > listanum[-1]:
        listanum.append(num)
        print('nº adicionado no final da lista')
    else:
        for i in range(5):
            if num <= listanum[i]:
                listanum.insert(i, num)
                print('nº adicionado na posição {0}'.format(i))
                break
    print(listanum) 

