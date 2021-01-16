'''
num = int(input('Digite um valor para a conversão: '))
print('[1] Conversão para binario')
print('[2] Conversão para Octal')
print('[3] Conversão para Hexadecimal')
a = int(input('Digite um numero de 1 a 3: '))
con = ''
if a == 1:
    while num > 0:
        resto = num % 2
        con = str(resto) + con
        num = num // 2
    print('O valor {} na sua conversão para a base decimal sera {}'.format(num, con))
elif a == 2:
    while num > 0:
        resto = num % 8
        con = str(resto) + con
        num // 8
    print('O valor {} na sua conversão para a base octal sera de {}'.format(num, con))
elif a == 3:
    while num > 0:
        resto = num % 16
        con = str(resto) + con
        num // 16
    print('O valor {} na sua conversão para a base hexadecimal sera de {}'.format(num, con))
else:
    print('O valor de entrada é invalido')
'''
num = int(input('Digite um valor para a conversão: '))
print('[1] Conversão para binario')
print('[2] Conversão para Octal')
print('[3] Conversão para Hexadecimal')
a = int(input('Digite um numero de 1 a 3: '))
if a == 1:
    print('O valor {} na sua conversão para a base decimal sera {}'.format(num, bin(num)[2:]))
elif a == 2:
    print('O valor {} na sua conversão para a base octal sera de {}'.format(num, oct(num)[2:]))
elif a == 3:
    print('O valor {} na sua conversão para a base hexadecimal sera de {}'.format(num, hex(num)[2:]))
else:
    print('O valor de entrada é invalido')