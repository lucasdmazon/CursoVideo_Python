nums = list()
while True:
    nums.append(int(input('Digite um valor: ')))
    if nums.count(nums[-1]) > 1:
        print('Valor duplicado! Não vou adicionar...')
        nums.pop()
    else:
        print('Valor adicionado com sucesso...')
    while True:
        res = str(input('Quer continuar [S/N]: ')).upper().split()[0]
        if res == 'S' or res == 'N':
            break
    if res == 'N':
        break
print('-=-' * 20)
print(f'Você digitou os valores {sorted(nums)}')


'''
nums = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in nums:
        nums.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        res = str(input('Quer continuar [S/N]: ')).upper().split()[0]
        if res == 'S' or res == 'N':
            break
    if res == 'N':
        break
print('-=-' * 20)
print(f'Você digitou os valores {sorted(nums)}')
'''
