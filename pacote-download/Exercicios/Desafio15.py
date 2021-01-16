from math import hypot
a = float(input('{}Digite o cateno oposto: '.format('\033[1;36m')))
b = float(input('Digite o cateto adjacente: '))
c = hypot(a, b)
print('{}O comprimento da hipotenusa do triangulo é de {:.2f}'.format('\033[1;30m', c))