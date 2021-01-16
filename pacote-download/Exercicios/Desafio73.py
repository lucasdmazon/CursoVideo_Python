time = ('ATLÉTICO-MG', 'INTERNACIONAL', 'FLAMENGO', 'SÃO PAULO', 'PALMEIRAS', 'SANTOS', 'GRÊMIO', 'FLUMINENSE', 'ATHLETICO', 'BAHIA', 'BRAGANTINO', 'BRAGANTINO', 'SPORT', 'CEARÁ', 'CORINTHIANS', 'VASCO', 'ATLÉTICO-GO', 'BOTAFOGO', 'CORITIBA', 'GOIÁS')
print('-=-'*15)
'''
print('Lista de times brasileirão: ', end='')
for t in time:
    print(f'{t}', end=", ")
print('\n', end="")
print('-=-'*15)
'''
print(f'Lista de times brasileirão: {time}')
print('-=-'*15)
print(f'Os 5 primeiros são: {time[0:5]}')
print('-=-'*15)
print(f'os 4 ultimos são: {time[-4:]}')
print('-=-'*15)
print(f'Times em Ordem Alfabetica: {sorted(time)}')
print('-=-'*15)
for c in range(0, len(time)):
    if time[c] == 'CHAPECOENSE':
        posicao = c + 1
        break
    else:
        posicao = 0
print(f'O Chapecoense está na {posicao}ª posição')

'''print(f'O Chapecoense está na {time.index("CHAPECOENSE") + 1}ª posição')'''

