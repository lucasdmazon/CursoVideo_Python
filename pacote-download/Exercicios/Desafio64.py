n = cont = soma = 0
while n != 999:
    n = int(input('Digite um valor [999 para parar]: '))
    soma += n
    cont += 1
    if n == 999:
        soma -= 999
        cont -= 1
print('Você digitou {} e a soma entre eles é {}'.format(cont, soma))
'''
n = cont = soma = 0
n = int(input('Digite um valor [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um valor [999 para parar]: '))
print('Você digitou {} e a soma entre eles é {}'.format(cont, soma))
'''