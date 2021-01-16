matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = 0
maior = 0
for l in range(0, 3):
    for a in range(0, 3):
        matriz[l][a] = int(input(f'Digite um valor para [{l}, {a}]: '))
print('-='*30)
for r in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[r][i]:^5}]', end='')
        '''
        if matriz[r][i] % 2 == 0:
            somap += e
        '''
    print()
print('-='*30)
for d in matriz:
    for e in d:
        if e % 2 == 0:
            somap += e
print(f'A soma dos valores pares é {somap}')

somat = matriz[0][2] + matriz[1][2] + matriz[2][2]
'''
for k in range(0, 3):
    somat += matriz[k][2]
'''
print(f'A soma dos valores da terceira coluna é {somat}.')

for f in matriz[1]:
    if maior == 0 or f > maior:
        maior = f
print(f'O maior valor da segunda linha é {maior}')
