'''
nome = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezeseis', 'Dezezete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente Novamente. ', end='')
print(f'Você digitou o numero {nome[num]}')
'''
nome = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezeseis', 'Dezezete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        num = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente Novamente. ', end='')
    print(f'Você digitou o numero {nome[num]}')
    while True:
        check = str(input('Quer Continuar: [S/N]: ')).upper().split()[0]
        if check in 'SN':
            break
    if check == 'N':
        break
