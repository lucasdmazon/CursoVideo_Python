from random import randint
from time import sleep
print('-'*30)
print(f'{"jOGO NA MEGA SENA":^30}')
print('-'*30)
i = 0
jogos = []
palpite = []
vezes = int(input('Quantos jogos você quer que eu sorteie? '))
while i < vezes:
    palpite = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    for c, v in enumerate(palpite):
        if palpite.count(v) > 1:
            palpite[c] = randint(1, 60)
    '''
    while True:
        num = randint(1, 60)
        if num not in palpite:
            palpite.append(num)
            cont += 1
        if cont >= 6:
            break   
    '''
    jogos.append(sorted(palpite[:]))
    i += 1
print('-='*4, end='')
print(f'{"  SORTEANDO 4 JOGOS  ":^10}', end='')
print('-='*4)
i = 0
while i < vezes:
    print(f'Jogo {i+1}: {jogos[i]}')
    sleep(1)
    i += 1
print('-=' * 4, end='')
print(f'{"  < BOA SORTE! >  ":^10}', end='')
print('-='*4)
