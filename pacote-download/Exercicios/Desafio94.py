lista = []
dados = {}
soma = 0
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
        if sexo in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    lista.append(dados.copy())
    del dados['nome']
    del dados['sexo']
    del dados['idade']

    while True:
        res = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if res in 'SN':
            break
        print('ERRO! responda apenas S ou N.')
    if res in 'N':
        break

print('-='*30)
print(f'A) O grupo tem {len(lista)} pessoas')
media = soma/len(lista)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print(f'\nD) Lista de pessoas acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print('\n', end='')
print('<<  ENCERRADO  >>')
