a = int(input('{}Digite o valor A: '.format('\033[1;33m')))
b = int(input('Digite o valor B: '))
c = int(input('Digite o valor C: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('{}O menor valor é {}, e o maior valor é {}'.format('\033[1;30m', menor, maior))

'''
if a < b < c:
    menor = a
    maior = c
    i = 1
elif a < c < b:
    menor = a
    maior = b
    i = 1
elif b < a < c:
    menor = b
    maior = c
    i = 1
elif b < c < a:
    menor = b
    maior = a
    i = 1
elif c < a < b:
    menor = c
    maior = b
    i = 1
elif c < b < a:
    menor = c
    maior = a
    i = 1
elif a == b:
    print('Os valores A e B são iguais')
    i = 0
elif a == c:
    print('Os valores A e C são iguais')
    i = 0
elif b == c:
    print('os valores B e C são iguais')
    i = 0

if i == 1:
    print('O menor valor é {}, e o maior valor é {}'.format(menor, maior))
'''
