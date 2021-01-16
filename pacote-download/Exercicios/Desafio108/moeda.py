def metade(n=0):
    resul = n/2
    return resul


def dobro(n=0):
    resul = n*2
    return resul


def aumentar(n=0, por=0):
    val = n * (por/100)
    resul = n + val
    return resul


def diminuir(n=0, por=0):
    val = n * (por/100)
    resul = n - val
    return resul


def moeda(val=0, moeda='R$'):
    val = str(f'{moeda}{val:.2f}')
    return val.replace('.', ',')

