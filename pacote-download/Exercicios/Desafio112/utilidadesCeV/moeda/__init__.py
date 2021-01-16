def metade(n, res=False):
    resul = n/2
    if res:
        resul = str(f'R${resul:.2f}').replace('.', ',')
    return resul


def dobro(n, res=False):
    resul = n*2
    if res:
        resul = str(f'R${resul:.2f}').replace('.', ',')
    return resul


def aumentar(n, por, res=False):
    val = n * (por/100)
    resul = n + val
    if res:
        resul = str(f'R${resul:.2f}').replace('.', ',')
    return resul


def diminuir(n, por, res=False):
    val = n * (por/100)
    resul = n - val
    if res:
        resul = str(f'R${resul:.2f}').replace('.', ',')
    return resul


def moeda(val):
    val = str(f'R${val:.2f}')
    return val.replace('.', ',')


def resumo(n=0, a=10, r=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço Analisado: \t{moeda(n)}')
    print(f'Dobro do Preço: \t{dobro(n, True)}')
    print(f'Metade do Preço: \t{metade(n, True)}')
    print(f'{a}% de Aumento: \t{aumentar(n, a, True)}')
    print(f'{r}% de Redução: \t{diminuir(n,r, True)}')
    print('-'*40)
