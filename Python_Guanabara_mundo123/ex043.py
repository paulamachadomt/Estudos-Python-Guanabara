#cálculo do imc e classificação
peso = float(input('informe o seu peso (kg): '))
altura = float(input('informe a sua altura (m): '))
imc = peso / (altura ** 2)
print('seu IMC é de: {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso normal')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')