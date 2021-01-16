from time import sleep
'''

def contador():
    for i in range(0, 3):
        if i == 0:
            inicio = 1
            fim = 10
            passo = 1
        elif i == 1:
            inicio = 10
            fim = 0
            passo = 2
        else:
            print('Agora é sua vez de personalizar a contagem!')
            inicio = int(input('Início: '))
            fim = int(input('Fim:    '))
            passo = int(input('Passo:  '))
        print('-='*20)
        if passo == 0:
            passo = 1
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        sleep(2)
        if inicio > fim:
            if passo > 0:
                passo = -passo

        if passo > 0:
            fim += 1
        if passo < 0:
            fim -= 1
        for j in range(inicio, fim, passo):
            print(j, end=' ')
            sleep(0.5)
        print('FIM!')
        print('-='*20)


contador()
'''


def contador(inicio, fim, passo):
    print('-='*20)
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2)
    if inicio > fim:
        if passo > 0:
            passo = -passo

    if passo > 0:
        fim += 1
    if passo < 0:
        fim -= 1
    for j in range(inicio, fim, passo):
        print(j, end=' ')
        sleep(0.5)
    print('FIM!')
    print('-='*20)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)
