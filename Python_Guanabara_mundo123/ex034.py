#calcula o aumento do salario de acordo com a faixa salarial
salario = float(input('informe o salário do funcionário: '))
if salario > 1250:
    novo_salario = salario + (salario * 10 / 100) #aumento de 10%
else:
    novo_salario = salario + (salario * 15 / 100) #aumento de 15%
print('Faixa de reajustes: salários até R$1250 recebem 15% de aumento; acima recebem 10%.')
print('O funcionário que recebia R${:.2f} reais, agora passa a receber R${:.2f} reais'.format(salario, novo_salario))
