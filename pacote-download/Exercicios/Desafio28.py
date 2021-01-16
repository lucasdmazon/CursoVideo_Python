from random import randint
from time import sleep
num = randint(0, 5)
print('-=-' * 20)
print('{}Vou pensar em um numero entre 0 a 5. Tente adivinhar...{}'.format('\033[1;34m', '\033[m'))
print('-=-' * 20)
res = int(input('{}Em que numero pensei: {}'.format('\033[1;35m', '\033[m')))
print('Processando...')
sleep(3)
if res == num:
    print('{}Você venceu, o numero era {}'.format('\033[1;34m', num))
else:
    print('{}Você perdeu, o numero era {}'.format('\033[1;31m', num))
