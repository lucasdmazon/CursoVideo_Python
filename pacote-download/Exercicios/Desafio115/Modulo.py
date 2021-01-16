def titulo(texto):
    print('-' * 40)
    print(f'{texto.center(42)}')
    print('-' * 40)


def ler(arquivo, tipo):
    try:
        arquivo = open(arquivo, tipo)
    except:
        arquivo = open(arquivo, 'w')
        print('\033[31mArquivo criado pois não  existia\033[m')
    else:
        print(arquivo.read())
        arquivo.close()


def escrever(arquivo, tipo, nome, idade):
    try:
        arquivo = open(arquivo, tipo)
    except:
        arquivo = open(arquivo, 'w')
        print('\033[31mArquivo criado pois não  existia\033[m')
    else:
        arquivo.write(f'{nome:<30}{idade} anos\n')
        arquivo.close()
