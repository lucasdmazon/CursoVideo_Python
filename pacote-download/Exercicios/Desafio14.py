import math
num = float(input('{}Digite um numero real: '.format('\033[1;34m')))
a = math.floor(num)
'''
a = math.trunc(num) 
'''
print('{}O numero {} tem a parte inteira {}'.format('\033[1;30m', num, a))