nome = str(input('{}Digite o nome da sua cidade: '.format('\033[1;36m'))).strip()
nome = nome.upper()
if nome[:5] == 'SANTO':
    print('{}Sua cidade começa com a palavra santo.'.format('\033[1;34m'))
else:
    print('{}Sua cidade não começa com a palavra santo.'.format('\033[1;31m'))
