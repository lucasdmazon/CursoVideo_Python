'''
cont = 0
posicao = -1
par1 = ''
par2 = ''
par3 = ''
par4 = ''
n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
n3 = int(input('Digite o 3° valor: '))
n4 = int(input('Digite o 4° valor: '))
tupla = (n1, n2, n3, n4)
for c in range(0, len(tupla)):
    if tupla[c] == 9:
        cont += 1

    if posicao == -1 and tupla[c] == 3:
        posicao = c + 1

    if c == 0 and tupla[c] % 2 == 0:
        par1 = tupla[c]

    if c == 1 and tupla[c] % 2 == 0:
        par2 = tupla[c]
    if c == 2 and tupla[c] % 2 == 0:
        par3 = tupla[c]
    if c == 3 and tupla[c] % 2 == 0:
        par4 = tupla[c]

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {cont} vezes')
if posicao != -1:
    print(f'O 3 foi digitado pela 1ª vez na {posicao}ª posição ')
else:
    print('O 3 não foi digitado em nenhuma posição')
print(f'Os valores pares foram: {par1} {par2} {par3} {par4}')
'''

num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais numero: ')),
       int(input('Digite o ultimo numero: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='  ')
