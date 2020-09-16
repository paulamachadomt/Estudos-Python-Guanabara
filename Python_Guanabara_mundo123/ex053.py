#verifica se a frase é um palíndromo
frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split() #retirar os espaços entre as palavras
junto = ''.join(palavras) #juntar as palavras sem os espaços entre elas
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('palíndromo')
else:
    print('não é palíndromo')

