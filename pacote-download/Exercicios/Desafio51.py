print('='*20)
print('Razão de uma PA')
print('='*20)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
print(primeiro, end=' -> ')
resul = primeiro
for i in range(primeiro, primeiro + 9):
    resul += razão
    print(resul, end=' -> ')
print('Acabou')


'''
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razão
for i in range(primeiro, decimo + razão, razão):
    resul = resul + razão
    print(resul, end=' -> ')
print('Acabou')
'''