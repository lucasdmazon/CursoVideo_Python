nums = []
pares = []
impares = []
while True:
    nums.append(int(input('Digite um valor: ')))
    while True:
        res = str(input('Quer continuar [S/N]: ')).upper().split()[0]
        if res in 'SN':
            break
    if res == 'N':
        break
for v in nums:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=-' * 20)
print(f'A lista completa é: {nums}')
print(f'A lista de pares é: {pares}')
print(f'A lista de impares é:{impares}')
