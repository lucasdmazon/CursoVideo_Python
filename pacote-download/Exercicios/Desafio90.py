dic = {}
dic['nome'] = str(input('Nome: '))
dic['media'] = float(input(f'Média de {dic["nome"]}: '))
if dic['media'] >= 7:
    dic['situação'] = 'Aprovado'
elif 5 <= dic['media'] < 7:
    dic['situação'] = 'Recuperação'
else:
    dic['situação'] = 'Reprovado'
for i, v in dic.items():
    print(f'{i} é igual a {v}')

