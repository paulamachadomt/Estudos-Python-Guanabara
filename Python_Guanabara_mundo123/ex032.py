#indica se o ano digitado é bissexto ou não
from datetime import date
ano = int(input('digite o ano que deseja verificar. Para o ano atual, digite 0: '))
if ano == 0:
    ano = date.today().year #seleciona o atual da data do computador
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('o ano {} É bissexto.'.format(ano))
else:
    print('o ano {} NÃO É bissexto.'.format(ano))