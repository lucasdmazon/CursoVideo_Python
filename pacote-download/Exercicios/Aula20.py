def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)


def contador(* num):
    '''
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
    '''
    tam = len(num)
    print(f'recebi os valores {num} e são ao todo {tam} números')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


def somat(* num):
    s = 0
    for n in num:
        s += n
    print(f'Somando os valores {num} a soma da {s}')


titulo('  CURSO EM VIDEO  ')
titulo('  APRENDA PYTON  ')
titulo('  GUSTAVO GUANABARA  ')

soma(b=4, a=5)
soma(8, 9)
soma(2, 1)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

print()

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

print()

somat(2, 4, 7)
somat(7, 8, 9, 0, 1)
