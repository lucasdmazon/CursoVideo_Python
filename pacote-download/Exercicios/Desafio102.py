def fatorial(n, show='False'):
    '''
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    print('-' * 30)
    fat = 1
    while n > 0:
        fat *= n
        if show:
            print(f'{n}', end=' ')
            if n > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        n -= 1
    return fat


print(fatorial(5, show=True))
help(fatorial)
