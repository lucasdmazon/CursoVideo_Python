import Modulo
from time import sleep
while True:
    Modulo.titulo('MENU PRINCIPAL')
    print('\033[32m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[32m2\033[m - \033[34mCadastrar nova pessoa\033[m')
    print('\033[32m3\033[m - \033[34msair do Sistema\033[m')
    print('-'*40)
    try:
        op = int(input('\033[32mSua opção: \033[m'))
    except:
        print('\033[31mErro na escolha! Tente Novamente\033[m')
    else:
        if op == 1:
            Modulo.titulo('PESSOAS CADASTRADAS')
            Modulo.ler('banco.txt', 'r+')
            sleep(1)
        elif op == 2:
            Modulo.titulo('NOVO CADASTRO')
            while True:
                nome = str(input('Nome: ')).strip()
                if nome == '':
                    print('\033[31mErro no preenchimento do campo! Tente Novamente\033[m')
                else:
                    break
            while True:
                try:
                    idade = int(input('Idade: '))
                except:
                    print('\033[31mErro no preenchimento do campo! Tente Novamente\033[m')
                else:
                    break
            Modulo.escrever('banco.txt', 'a+', nome, idade)
            print(f'Novo registro de {nome} adicionado.')
            sleep(1)
        elif op == 3:
            Modulo.titulo('Saindo do Sistema... Até logo!')
            sleep(1)
            break
        else:
            print('\033[31mErro na escolha! Tente Novamente\033[m')
