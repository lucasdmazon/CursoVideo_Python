from random import randint
from time import sleep
'''
from operator import itemgetter
'''
dic = {}
cont = 1
print('Valores sorteados:')
for i in range(1, 5):
    dic[f'jogador{i}'] = randint(1, 6)
    print(f'   O jogador{i} tirou {dic[f"jogador{i}"]}')
    sleep(1)
print('Ranking dos jogadores: ')
'''
ranking = dict()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) 
'''
for g in sorted(dic, key=dic.get):
    print(f'    {cont}° lugar: {g} com {dic[g]}')
    sleep(1)
    cont += 1
