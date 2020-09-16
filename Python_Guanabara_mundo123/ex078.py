#maior e menor valor dentro de uma lista
listanum = []
maior = 0
menor = 0
posicaoMaior = 0
posicaoMenor = 0
for c in range(0, 5):
    listanum.append(int(input(f"digite um valor para posição {c}: ")))
posicaoMaior = listanum.index(max(listanum))
posicaoMenor = listanum.index(min(listanum))
print('=-' * 30)
print(f"você digitou os valores {listanum}")
print(f'o maior valor digitado foi {max(listanum)}, na posição {posicaoMaior}')
print(f'o menor valor digitado foi {min(listanum)}, na posição {posicaoMenor}')