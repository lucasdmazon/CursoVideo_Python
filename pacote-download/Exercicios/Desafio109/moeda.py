def metade(n, res=False):
    resul = n/2
    if res:
        resul = str(f'R${resul:.2f}').replace('.', ',')
    return resul
    '''return resul if format=Flase else moeda(resul) '''


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
