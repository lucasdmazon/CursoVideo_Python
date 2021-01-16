from datetime import date
ano = int(input('{}Que ano você quer analisar? Coloque 0 para analsar o ano atual: '.format('\033[1;32m')))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}{} é um ano bissexto'.format('\033[1;30m', ano))
else:
    print('{}{} não é um ano bissexto'.format('\033[1;30m', ano))