#tabuada
n = 0
while True:
    num = int(input('Qual tabuada você quer ver? '))
    if num < 0:
        break
    print('-' * 30)
    for c in range(1,11):
        print(f'{num} X {c} = {num*c}')
    print('-' * 30)
print('PROGRAMA DE TABUADA FINALIZADO')