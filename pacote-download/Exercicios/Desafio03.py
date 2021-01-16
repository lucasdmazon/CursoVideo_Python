num = int(input('{}Digite um numero: {}'.format('\033[1;32m', '\033[m')))
print('{}Sucessor: {}'.format('\033[1;36m', num+1), end=" e ")
print('Antecessor: {}'.format(num-1))