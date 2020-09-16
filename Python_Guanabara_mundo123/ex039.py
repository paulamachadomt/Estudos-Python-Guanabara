#cálculo do período de alistamento militar de acordo com a idade
from datetime import date
ano_nasc = int(input('informe o ano que você nasceu: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print('você tem {} anos em {}.'.format(idade, ano_atual))
if idade > 18:   
    saldo = idade - 18 
    ano = ano_atual - saldo
    print('você já deveria ter se alistado há {} ano(s).'.format(saldo))
    print('seu alistamento deveria ter sido em {}'.format(ano))
elif idade == 18:
    print('seu alistamento é este ano ({}).'.format(ano_atual))
elif idade < 18:
    saldo = 18 - idade
    ano = ano_atual + saldo
    print('Ainda faltam {} ano(s) para seu alistamento, que será em {}.'.format(saldo, ano))
    