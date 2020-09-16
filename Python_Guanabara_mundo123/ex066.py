#usando while infinito e break
soma = contador = n = 0
while True:
    n = int(input('digite um valor [999 para finalizar]: '))
    if n == 999:
        break
    soma += n
    contador += 1
print(f'Você digitou {contador} valores e soma entre eles foi {soma}.') 