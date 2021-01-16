dic = {}
gols = []
i = total = 0
dic['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
while i < partidas:
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
    i += 1
    total += gols[-1]
dic['gols'] = gols[:]
dic['total'] = total
print('-='*30)
print(dic)
print('-='*30)
for i, v in dic.items():
    print(f'O campo {i} tem o valor {v}.')
print('-='*30)
print(f'O jogador {dic["nome"]} jogou {len(dic["gols"])} partidas.')
for g, a in enumerate(dic["gols"]):
    print(f'    => Na partida {g}, fez {a} gols.')
print(f'Foi um total de {total} gols.')
