from random import randint
cont = 0
print('-=-' * 10)
print('Vamos Jogar Par ou Impar')
print('-=-' * 10)
while True:
    while True:
        n = int(input('Digite um valor: '))
        if n >= 0 and n <= 10:
            break
    while True:
        escol = str(input('Par ou Impar? [P/I]')).upper().strip()[0]
        if escol == 'P' or escol == 'I':
            break
    comp = randint(0, 10)
    soma = n + comp
    if soma % 2 == 0:
        resul = 'PAR'
    else:
        resul = 'IMPAR'
    print('-' * 30)
    print(f'Você jogou {n} e o computador jogou {comp}. Total de {soma}, deu {resul}')
    print('-' * 30)
    if escol == 'P' and resul == 'PAR':
        print('Você Venceu')
        print('Vamos Jogar Novamente...')
        print('-=-' * 10)
        cont += 1
    elif escol == 'I' and resul == 'IMPAR':
        print('Você Venceu')
        print('Vamos Jogar Novamente...')
        print('-=-' * 10)
        cont += 1
    else:
        print('Você Perdeu')
        print('-=-' * 10)
        print(f'Ganhou um total de {cont} partida(s)')
        break
