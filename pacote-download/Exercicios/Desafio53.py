frase = str(input('Digite uma frase: ')).strip().lower()
a = ''.join(frase.split())
b = a[::-1]
print('O inverso de {} é {}'.format(a, b))
if a == b:
    print('É um palindromo')
else:
    print('Não é um palindromo')

'''
frase = str(input('Digite uma frase: ')).strip().upper()
junto = ''.join(frase.split())
inverso = ''
for letra in range (len(junto) - 1 -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('É um palindromo')
else:
    print('Não é um palindromo')
'''