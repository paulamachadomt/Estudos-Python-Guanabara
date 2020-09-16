#classificação de atletas
from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('informe o ano de nascimento: '))
idade = ano_atual - ano_nasc
print('o atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('classificação: MIRIM')
elif idade <= 14:
    print('classificação: INFANTIL')
elif idade <=19:
    print('classificação: JUNIOR')
elif idade <= 25:
    print('classificação: SÊNIOR')
else:
    print('classificação: MASTER')