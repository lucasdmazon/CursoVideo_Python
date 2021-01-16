from datetime import date
anoatual = date.today().year
anonasc = int(input('Digite seu ano de nascimento: '))
idade = anoatual - anonasc
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação INFANTIL')
elif idade <= 19:
    print('Classificação JUNIOR')
elif idade <= 20:
    print('Classificação SÊNIOR')
else:
    print('Classificação MASTER')