from random import randint
from time import sleep
res = ''
cont = 0
num = randint(0, 10)
print('-=-' * 20)
print('{}Vou pensar em um numero entre 0 a 10. Tente adivinhar...{}'.format('\033[1;34m', '\033[m'))
print('-=-' * 20)
while res != num:
    res = int(input('{}Em que numero pensei: {}'.format('\033[1;35m', '\033[m')))
    print('Processando...')
    sleep(3)
    if res == num:
        print('{}Você venceu, o numero era {}, mas você precisou de {} tentativas para descobrir'.format('\033[1;34m', num, cont))
    elif res > num:
        print('{}Você errou, tente um numero MENOR'.format('\033[1;31m'))
        cont += 1
    elif res < num:
        print('{}Você errou, tente um numero MAIOR'.format('\033[1;31m'))
        cont += 1
