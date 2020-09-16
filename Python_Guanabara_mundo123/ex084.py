pessoas = []
dados = []
continuar = ''
maior = 0
menor = 0
while True:
    dados.append(input('Informe o nome: '))
    dados.append(float(input('Informe o peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()    
    continuar = input('Deseja continuar? [s/n]').upper()
    if continuar in "Nn":
        break
print('-'*40)
print(f'Os dados foram: {pessoas}')
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'Maior peso: {maior} e menor peso: {menor}')
