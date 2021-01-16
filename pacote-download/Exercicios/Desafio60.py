'''
val = int(input('Digite um valor: !'))
resul = 1
for c in range(val, 1, -1):
    resul *= c
print('O {}! é igual a {}'.format(val, resul))
'''

'''
from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: ')
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))
'''
from time import sleep
val = int(input('Digite um valor: '))
resul = 1
i = val
print('Calculando {}! = '.format(val),end='')
sleep(1)
while i > 0:
    print(i, end='')
    if i > 1:
        print(' X ', end='')
    else:
        print(' = ', end='')
    resul *= i
    i -= 1
print('{}'.format(resul))
