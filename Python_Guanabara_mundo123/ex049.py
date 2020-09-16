#imprimir a tabuada de um número
numero = int(input('Qual tabuada você quer ver? Digite um número inteiro: '))
for c in range(1, 11):
    print('{} X {} = {}'.format(numero, c, numero * c))
