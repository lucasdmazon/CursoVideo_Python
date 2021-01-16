num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
sorted(num, reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print(f'Não achei o numero 4')
#num.pop(2)
print(num)
print(f'Esta lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')


a = [2, 3, 4, 7]
b = a
#b = a[:]
b[2] = 8
print(a)
print(b)

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for v in valores:
    print(f'{v}...', end='')
