#cálculo de aumento salarial
salario = float(input('Digite o salário do funcionário: R$ '))
novo_salario = salario + (salario * 15 / 100)
print('Com 15% de aumento, o funcionário que recebia R${:.2f}, passa a receber R${:.2f}'.format(salario, novo_salario))
