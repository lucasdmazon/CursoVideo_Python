from random import sample
a = str(input('{}Digite o nome do primeiro aluno: '.format('\033[1;33m')))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
mod = [a, b, c, d]
e = sample(mod, k=4)
'''
e = shuffle(mod)
'''
print('{}A ordem de apresentação sera {}'.format('\033[1;30m', e))
