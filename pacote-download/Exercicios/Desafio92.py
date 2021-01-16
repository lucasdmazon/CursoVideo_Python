from datetime import date
dic = {}
dic['nome'] = str(input('Nome: '))
ano = date.today().year
anonasc = int(input('Ano de Nascimento: '))
dic['idade'] = ano - anonasc
dic['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dic['ctps'] != 0:
    dic['contratação'] = int(input('Ano de Contratação: '))
    dic['salário'] = float(input('Salário: R$'))
    dic['aposentadoria'] = (35 - (ano - dic['contratação'])) + dic['idade']
print('-='*30)
for i, v in dic.items():
    print(f'  - {i} tem o valor {v}')
