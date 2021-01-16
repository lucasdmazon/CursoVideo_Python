nome = str(input('{}Digite seu nome completo: '.format('\033[1;36m'))).strip().split()
print('{}Muito prazer em te conhecer!'.format('\033[1;30m'))
print('Primeiro: {}'.format(nome[0]))
print('Ultimo: {}'.format(nome[-1]))
