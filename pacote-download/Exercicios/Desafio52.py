n = int(input('Digite um numero: '))
a = 0
for i in range(2, n):
    if n % i == 0:
        a = 1
if a == 1:
    print('Este numero não é primo')
else:
    print('Este numero é primo')


'''
n = int(input('Digite um numero: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} ', c, end='')
print('\n\033[mO numero {} foi divisel {}'.format(n, tot))
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')
'''