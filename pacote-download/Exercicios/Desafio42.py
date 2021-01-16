print('-=-' * 20)
print('{}Analisador de Triângulos{}'.format('\033[1;32m', '\033[m'))
print('-=-' * 20)
a = float(input('{}Digite o valor da primeira reta: '.format('\033[1;36m')))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('{}As três retas podem formar um triangulo '.format('\033[1;34m'), end='')
    if a == b == c:
        print('equilátero')
    elif a != b and b != c and a != c:
        print('escaleno')
    else:
        print('isóceles')
else:
    print('{}As três retas não podem formar um triangulo'.format('\033[1;31m'))
