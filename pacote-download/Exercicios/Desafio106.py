from time import sleep


def cabeçalho(titulo, cor=0):
    print(f'\033[0;{cor}m', end='')
    titulo = f' {titulo} '
    print('~'*len(titulo))
    print(titulo)
    print('~'*len(titulo))
    print('\033[m', end='')
    sleep(1)


while True:
    cabeçalho('SISTEMA DE AJUDA PyHELP', 33)
    fun = str(input('Função ou Biblioteca > '))
    if fun.upper() == 'FIM':
        cabeçalho('ATÉ LOGO!', 31)
        break
    cabeçalho(f"Acessando o manual do comando '{fun}'", 34)
    sleep(1)
    print('\033[0;30m', end='')
    print(help(fun))
    print('\033[m', end='')
    sleep(1)
