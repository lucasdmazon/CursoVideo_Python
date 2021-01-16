from random import randint
'''
num1 = randint(1, 10)
num2 = randint(1, 10)
num3 = randint(1, 10)
num4 = randint(1, 10)
num5 = randint(1, 10)
n = (n1, n2, n3, n4, n5)

for c in range(0, len(n)):
    if maior == 0 or n[c] > maior:
        maior = n[c]
    if menor == 0 or n[c] < menor:
        menor = n[c]
'''

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end=' ')
for i in n:
    print(f'{i}', end=' ')
print(f'\nMenor Valor: {min(n)}')
print(f'Maior valor: {max(n)}')
