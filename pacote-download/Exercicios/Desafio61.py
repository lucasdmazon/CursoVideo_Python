print('='*20)
print('Razão de uma PA')
print('='*20)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
cont = 1
while cont <= 10:
    if cont == 1:
        print(0, end=' -> ')
    print(primeiro, end=' -> ')
    primeiro += razão
    cont += 1
print('Acabou')