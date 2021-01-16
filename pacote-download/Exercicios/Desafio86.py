matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for a in range(0, 3):
        matriz[l][a] = int(input(f'Digite um valor para [{l}, {a}]: '))
print('-='*30)
for g in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[g][i]:^5}]', end='')
    print()
