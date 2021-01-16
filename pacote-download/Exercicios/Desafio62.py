print('='*20)
print('Razão de uma PA')
print('='*20)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
cont = 1
a = 10
b = 0
extra = 0
while b == 0:
    while cont != a:
        if cont == 1:
            print(0, end=' -> ')
        print(primeiro, end=' -> ')
        primeiro += razão
        cont += 1
    if cont == a:
        extra = int(input('\nDigite quantos mais termos dessa PA você quer ver: '))
        a += extra
    if extra == 0:
        b = 1
print('Você calculou ao todo {} termos de uma PA'.format(a))
print('Concluido')
