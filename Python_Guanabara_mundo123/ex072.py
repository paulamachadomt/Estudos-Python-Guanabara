#início mundo 3 - TUPLAS
#números escritos por extenso
continuar = ''
contador = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:    
    while True:
        num = int(input('digite um número de 0 a 20: '))
        if 0 <= num <= 20:
            break
        print('nùmero inválido. digite novamente.')
    print(f'Você digitou o número: {contador[num]}')
    continuar = input('deseja continuar? S/N').strip().upper()
    if continuar in 'Nn':
        print('operação finalizada')
        break
