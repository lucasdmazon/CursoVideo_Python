frase = str(input('{}Digite uma frase: '.format('\033[1;34m'))).strip().upper()
print('{}A letra A aparece {} vezes'.format('\033[1;30m', frase.count('A')))
print('Ela aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('Ela aparece pela ultima vez na posição {}'.format(frase.rfind('A')+1))