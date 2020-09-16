#cálculo triângulo
print('=-=' * 20)
print('Analisador de Triângulos')
print('=-=' * 20)
reta1 = float(input('informe o tamanho da primeira reta: '))
reta2 = float(input('informe o tamanho da segunda reta: '))
reta3 = float(input('informe o tamanho da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO FORMAM um triângulo.')