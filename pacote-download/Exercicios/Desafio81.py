lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    while True:
        res = str(input('Quer continuar [S/N]: ')).upper().split()[0]
        if res == 'S' or res == 'N':
            break
    if res == 'N':
        break
print('-=-'*15)
print(f'Foram digitados {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 está na lista. E esta na posição: ', end='')
    for p, v in enumerate(lista):
        if v == 5:
            print(f'{p}')
else:
    print('O valor 5 não esta na lista.')
