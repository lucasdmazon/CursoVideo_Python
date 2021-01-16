nome = str(input('{}Digite seu nome completo: '.format('\033[1;34m')))
nome = nome.upper()
if nome.find('SILVA') >= 0:
    print('{}Você possui Silva no nome'.format('\033[1;36m'))
else:
    print('{}Você não possui Silva no nome'.format('\033[1;31m'))

'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper())
'''