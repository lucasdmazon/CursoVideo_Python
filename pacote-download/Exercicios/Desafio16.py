from math import sin, cos, tan
a = int(input('{}Digite o ângulo: '.format('\033[1;36m')))
sen = sin(a)
cos = cos(a)
tan = tan(a)
print('{}O valor do seno de {}° é de {:.2f}'.format('\033[1;30m', a, sen))
print('O valor do cosseno de {}° é de {:.2f}'.format(a, cos))
print('O valor da tangete de {}° é de {:.2f}'.format(a, tan))
