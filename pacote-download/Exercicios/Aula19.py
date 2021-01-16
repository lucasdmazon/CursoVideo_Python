pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
'''del pessoas['sexo']'''
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for g in pessoas.values():
    print(g)

for i, v in pessoas.items():
    print(f'{i} = {v}')

'''
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for l, o in e.items():
        print(f'O campo {l} tem valor {o}.')
'''
for e in brasil:
    for l in e.values():
        print(l, end=' ')
    print()
'''
