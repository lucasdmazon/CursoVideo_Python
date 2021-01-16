tabela = []
dic = {}
gols = []
i = total = cod = 0
print('-'*30)
while True:
    dic['cod'] = cod
    dic['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
    while i < partidas:
        gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
        i += 1
        total += gols[-1]
    dic['gols'] = gols[:]
    dic['total'] = total
    tabela.append(dic.copy())
    dic.clear()
    gols.clear()
    i = 0
    total = 0
    while True:
        res = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
        if res in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if res in 'N':
        break
    cod += 1
    print('-'*30)
print('-='*30)
print(f'{"cod"}', end='')
print(f'{"nome":^27}', end='')
print(f'{"gols"}', end='')
print(f'{"total":^20}', end='')
print('\n', end='')
print('-'*50)
for k, v in enumerate(tabela):
    for d in v.values():
        print(f'{str(d):<14}', end='')
    print()
print('-'*50)
while True:
    dad = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if dad == 999:
        break
    if dad > len(tabela):
        print(f'ERRO! não existe jogador com código {dad}! Tente novamente')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {tabela[dad]["nome"]}')
        for j, a in enumerate(tabela[dad]['gols']):
            print(f'    No jogo {j+1}, fez {a} gols.')
    print('-' * 50)
print('<< VOLTE SEMPRE >>')
