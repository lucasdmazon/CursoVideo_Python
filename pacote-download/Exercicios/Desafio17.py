'''
import random
a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
e = random.randint(1, 4)
if e == 1:
    print('{} ira apagar o quadro'.format(a))
elif e == 2:
    print('{} ira apagar o quadro'.format(b))
elif e == 3:
    print('{} ira apagar o quadro'.format(c))
elif e == 4:
    print('{} ira apagar o quadro'.format(d))
'''

from random import choice
a = str(input('{}Digite o nome do primeiro aluno: '.format('\033[1;33m')))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
mod = [a, b, c, d]
e = choice(mod)
print('{}O escolhido para limpar a lousa é {}{}'.format('\033[1;30m', '\033[31m', e))
