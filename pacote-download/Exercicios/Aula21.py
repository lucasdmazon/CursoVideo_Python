def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    '''


    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


def somar(a=0, b=0, c=0):
    '''
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return:
    '''
    s = a + b + c
    print(f'A soma vale {s}')


def funcao():
    '''
    global n1
    '''
    n1 = 4
    print(f'N1 vale {n1}')


def somar2(a=0, b=0, c=0):
    s = a + b + c
    return s


help(print)

print(print.__doc__)

help(contador)

somar(3, 2)

n1 = 2
funcao()
print(f'N1 vale {n1}')


r1 = somar2(3, 2, 5)
r2 = somar2(2, 2)
r3 = somar2(6)
print(f'Meus calculos deram {r1}, {r2}, {r3}')

