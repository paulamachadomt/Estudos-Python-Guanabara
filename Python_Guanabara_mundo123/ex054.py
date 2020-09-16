#calcula quantas pessoas tem mais de 21 anos e qtas têm menos
from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for c in range(1,8):
    ano = int(input('em que ano a pessoa nasceu?  '))
    idade = atual - ano
    if idade > 21:
        maiores = maiores + 1
    else:
        menores = menores + 1
print('{} pessoas tem mais de 21 anos e {} tem menos'.format(maiores, menores))