num = str(input('{}Digite um numero entre 0 a 9999: '.format('\033[1;35m'))).strip()
num = ''.join(num.split())
if len(num) == 1:
    print('Unidade: {}'.format(num[-1]))
elif len(num) == 2:
    print('Unidade: {}'.format(num[-1]))
    print('Dezena: {}'.format(num[-2]))
elif len(num) == 3:
    print('Unidade: {}'.format(num[-1]))
    print('Dezena: {}'.format(num[-2]))
    print('Centena: {}'.format(num[-3]))
elif len(num) == 4:
    print('Unidade: {}'.format(num[-1]))
    print('Dezena: {}'.format(num[-2]))
    print('Centena: {}'.format(num[-3]))
    print('Milhar: {}'.format(num[-4]))
else:
    print('O numero excede a quantidade de caracteres permitidos')

'''
num = str(input('Digite um numero entre 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 100
m = num // 1000 % 1000
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
'''