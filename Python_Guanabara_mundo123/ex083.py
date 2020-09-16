#validação expressão matemática
expressao = input('informe uma expressão matemática: ')
lista = []
for parenteses in expressao:
    if parenteses == '(':
        lista.append('(')
    elif parenteses == ')':
        if len(lista) > 0:
            lista.pop() #remove último item do vetor
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('expressão válida')
else:
    print('expressão inválida')