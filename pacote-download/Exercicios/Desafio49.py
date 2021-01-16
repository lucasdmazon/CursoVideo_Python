var = int(input('{}Digite um numero para ver sua tabuada: {}{}'.format('\033[1;35m', '\033[m', '\033[1;30m')))
tab =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('-'*12)
for d in tab:
    res = var * d
    print('{} x {:2} = {}'.format(var, tab[d], res))
print('-'*12)

'''
var = int(input('{}Digite um numero para ver sua tabuada: {}{}'.format('\033[1;35m', '\033[m', '\033[1;30m')))
print('-'*12)
for d in range(0, 11):
    res = var * d
    print('{} x {:2} = {}'.format(var, d, res))
print('-'*12)
'''