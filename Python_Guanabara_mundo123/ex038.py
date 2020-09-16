#verifica qual valor é maior - usando if, elif, else
num1 = int(input('digite um número inteiro: '))
num2 = int(input('digite outro número inteiro: '))
if num1 > num2:
    print("O PRIMEIRO valor é maior.")
elif num2 > num1:
    print("O SEGUNDO valor é maior.")
elif num1 == num2:
    print('Os dois valores são iguais')