#posição da primeira e última letra A na frase
frase = str(input('digite uma frase:')).strip().upper()
print('A frase que você digitou tem {} letras.'.format(len(frase)))
print("A letra 'A' aparece {} vezes na frase que você digitou.".format(frase.count('A')))
print("A primeira letra 'A' aparece na posição {}.".format(frase.find('A')+1))
print("A última letra 'A' aparece na posição {}.".format(frase.rfind('A')+1))
