from time import sleep
a = int(input('\033[1;34mDigite um valor: '))
b = int(input('Digite outro valor: '))
escolha = 0
while escolha != 5:
    print('\033[1;35m-=-'*8)
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos Numeros
    [5]Sair do programa
''')
    print('-=-' * 8)
    escolha = int(input('O que você quer: '))
    if escolha == 1:
        print('\033[1;32mA soma entre {} e {} é {}'.format(a, b, a+b))
        sleep(2)
    elif escolha == 2:
        print('\033[1;32mA multiplicação entre {} e {} é {}'.format(a, b, a*b))
        sleep(2)
    elif escolha == 3:
        if a > b:
            print('\033[1;32m{} é o maior valor'.format(a))
            sleep(2)
        elif b > a:
            print('\033[1;32m{} é o maior valor'.format(b))
            sleep(2)
        else:
            print('\033[1;32m{} e {} são iguais'.format(a, b))
            sleep(2)
    elif escolha == 4:
        print('\033[1;31mResetando Valores...')
        sleep(2)
        a = int(input('\033[1;34mDigite um valor: '))
        b = int(input('Digite outro valor: '))
    elif escolha == 5:
        print('\033[1;30mEntendido')
        sleep(2)
    else:
        print('\033[1;31mHouve um erro de digitação')
        sleep(2)
print('\033[1;30mDesligando...')
sleep(3)
