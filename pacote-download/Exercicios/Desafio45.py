from random import choice
from time import sleep
print('{}-=-'.format('\033[1;33m')*20)
print('JOKENPO')
print('-=-'*20)
print('{}'.format('\033[m'))
a = 'PEDRA'
b = 'TESOURA'
c = 'PAPEL'
i = [a, b, c]
usu = str(input('{}Escolha sua jogada: '.format('\033[1;36m'))).strip().upper()
comp = choice(i)
print('Jo')
sleep(0.75)
print('Ken')
sleep(0.75)
print('Po')
sleep(0.75)
print('{}-=-'.format('\033[35m')*20)
print('O jogador jogou {}'.format(usu))
print('O computador jogou {}'.format(comp))
print('-=-'*20)
if comp == usu:
    print('{}Houve empate'.format('\033[1;32m'))
elif comp == a and usu == 'PAPEL':
    print('{}Você venceu'.format('\033[1;34m'))
elif comp == a and usu == 'TESOURA':
    print('{}Eu venci'.format('\033[1;31m'))
elif comp == b and usu == 'PEDRA':
    print('{}Você venceu'.format('\033[1;34m'))
elif comp == b and usu == 'PAPEL':
    print('{}Eu venci'.format('\033[1;31m'))
elif comp == c and usu == 'PEDRA':
    print('{}Eu venci'.format('\033[1;31m'))
elif comp == c and usu == 'TESOURA':
    print('{}Você venceu'.format('\033[1;34m'))
else:
    print('{}Houve um erro de digitação. Tente Novamente'.format('\033[1;32m'))